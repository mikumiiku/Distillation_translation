'''
将在Xsum上微调过的Qwen2.5-1.5B-Instruct通过硬标签蒸馏方式蒸馏到Qwen2.5-0.5B-Instruct
'''
import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
import torch
from datasets import  DatasetDict
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    Seq2SeqTrainingArguments,
    Seq2SeqTrainer,
    DataCollatorForLanguageModeling,
    EarlyStoppingCallback,
)
from tqdm.auto import tqdm
import matplotlib.pyplot as plt
from data import load_and_prepare_dataset,preprocess_data,MAX_INPUT_LENGTH,MAX_TARGET_LENGTH
from peft import PeftModel,LoraConfig, get_peft_model, TaskType
from datasets import load_from_disk

# --- 全局设置 ---
device = torch.device("cuda")

TEACHER_MODEL_NAME = "Qwen/Qwen2.5-1.5B-Instruct"
TEACHER_MODEL_PATH = "./models/Qwen2.5_1.5B_Instruct"
STUDENT_MODEL_NAME = "Qwen/Qwen2.5-0.5B-Instruct"
STUDENT_MODEL_PATH = "./models/Qwen2.5_0.5B_Instruct"
LORA_PATH="./teacher_lora"


OUTPUT_DIR = "./HLKD_lora"
LOGGING_DIR = "./HLKD_lora/logs"
NUM_TRAIN_EPOCHS = 3
TRAIN_BATCH_SIZE = 1
EVAL_BATCH_SIZE =1
LEARNING_RATE = 4e-4
WEIGHT_DECAY = 0.03
WARMUP_RATIO=0.1
LOGGING_STEPS = 50

# LoRA 配置
LORA_R = 16
LORA_ALPHA = 32
LORA_DROPOUT = 0.2
LORA_TARGET_MODULES = [
    "q_proj",
    "k_proj",
    "v_proj",
    "o_proj",
    "gate_proj",
    "up_proj",
    "down_proj",
]

PROMPT_TEMPLATE = (
    "<|im_start|>system\nYou are a helpful assistant that translates english documents to chinese documents.<|im_end|>\n"
    "<|im_start|>user\nTranslate the following english document to chinese document without any explaination:\n{eng}\n<|im_end|>\n"
    "<|im_start|>assistant\n"
)



def load_model_and_tokenizer(is_teacher):
    """加载模型和分词器。"""
    tokenizer = AutoTokenizer.from_pretrained(
        TEACHER_MODEL_PATH if is_teacher else STUDENT_MODEL_PATH, 
        trust_remote_code=True, 
        padding_side="left"
    )

    model = AutoModelForCausalLM.from_pretrained(
        TEACHER_MODEL_PATH if is_teacher else STUDENT_MODEL_PATH, 
        torch_dtype=torch.bfloat16,
        device_map='auto',
        trust_remote_code=True,
        use_cache=is_teacher,
    )
    if is_teacher:
        model = PeftModel.from_pretrained(model, LORA_PATH)

    return model, tokenizer


def generate_teacher_summaries(teacher_model, teacher_tokenizer, dataset):
    split_name = dataset.split

    teacher_model.eval()
    teacher_summaries = []
    batch_size = EVAL_BATCH_SIZE

    progress_bar = tqdm(
        range(0, len(dataset), batch_size),
        desc=f"Generating translation: ({split_name})",
        unit="batch",
    )

    for i in progress_bar:
        batch_engs = dataset[i : min(i + batch_size, len(dataset))]["english"]
        prompts = [
            PROMPT_TEMPLATE.format(eng=eng) for eng in batch_engs
        ]

        inputs = teacher_tokenizer(
            prompts,
            return_tensors="pt",
            padding=True,
            truncation=True,
            max_length=MAX_INPUT_LENGTH,
        ).to(device)

        with torch.no_grad():
            outputs = teacher_model.generate(
                **inputs,
                max_new_tokens=MAX_TARGET_LENGTH,
                num_beams=4,
                early_stopping=True,
            )

        input_seq_len = inputs.input_ids.shape[1]
        generated_ids = outputs[:, input_seq_len:].cpu()
        batch_summaries = teacher_tokenizer.batch_decode(
            generated_ids, skip_special_tokens=True
        )
        teacher_summaries.extend([s.strip() for s in batch_summaries])

        del inputs, outputs, generated_ids
        torch.cuda.empty_cache()

    dataset_with_summaries = dataset.add_column("teacher_chinese", teacher_summaries)
    return dataset_with_summaries


def train_student_model(
    student_model,
    student_tokenizer,
    tokenized_datasets,
):
    """配置并运行学生模型的训练过程。"""
    training_args = Seq2SeqTrainingArguments(
        output_dir=OUTPUT_DIR,
        eval_strategy="epoch",
        logging_strategy="steps",
        logging_steps=LOGGING_STEPS,
        logging_dir=LOGGING_DIR,
        save_strategy="epoch",
        learning_rate=LEARNING_RATE,
        per_device_train_batch_size=TRAIN_BATCH_SIZE,
        per_device_eval_batch_size=EVAL_BATCH_SIZE,
        weight_decay=WEIGHT_DECAY,
        num_train_epochs=NUM_TRAIN_EPOCHS,
        warmup_ratio=WARMUP_RATIO,
        bf16=True,
        load_best_model_at_end=True,
        metric_for_best_model="eval_loss",
        greater_is_better=False,
        save_total_limit=2,
        label_names=["labels"],
        lr_scheduler_type="cosine",
    )

    data_collator = DataCollatorForLanguageModeling(
        tokenizer=student_tokenizer, mlm=False
    )

    trainer = Seq2SeqTrainer(
        model=student_model,
        args=training_args,
        train_dataset=tokenized_datasets["train"],
        eval_dataset=tokenized_datasets["eval"],
        data_collator=data_collator,
        callbacks=[EarlyStoppingCallback(early_stopping_patience=3)],
    )

    train_result = trainer.train()

    trainer.save_model()
    trainer.log_metrics("train", train_result.metrics)
    trainer.save_metrics("train", train_result.metrics)
    trainer.save_state()

    training_logs = [log for log in trainer.state.log_history if "step" in log and "loss" in log]
    steps = [log["step"] for log in training_logs]
    losses = [log["loss"] for log in training_logs]
    plt.figure(figsize=(10, 6))
    plt.plot(steps, losses, marker="o", linestyle="-", label="Training Loss")
    plt.title("Training Loss Curve")
    plt.xlabel("Steps")
    plt.ylabel("Loss")
    plt.grid(True)
    plt.legend()
    plot_path = os.path.join(OUTPUT_DIR, "training_loss_curve.png")
    plt.savefig(plot_path)
    plt.show()

    eval_metrics = trainer.evaluate()
    trainer.log_metrics("eval", eval_metrics)
    trainer.save_metrics("eval", eval_metrics)

    # Clean up GPU memory after training
    del student_model, trainer, data_collator
    torch.cuda.empty_cache()


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # 1. 加载和准备数据集
    raw_datasets = load_and_prepare_dataset()

    # 2. 生成包含硬标签的数据集
    teacher_model, teacher_tokenizer = load_model_and_tokenizer(
        is_teacher=True
    )

    ds_save_path = "./HLKD_tokenized_ds"
    if os.path.exists(ds_save_path):
        print(f"Loading tokenized datasets from {ds_save_path} ...")
        tokenized_datasets = DatasetDict.load_from_disk(ds_save_path)
    else:
        tokenized_datasets = DatasetDict({
            "train": preprocess_data(
                generate_teacher_summaries(teacher_model, teacher_tokenizer, raw_datasets["train"]),
                teacher_tokenizer, label='teacher_chinese'
            ),
            "eval": preprocess_data(
                generate_teacher_summaries(teacher_model, teacher_tokenizer, raw_datasets["eval"]),
                teacher_tokenizer, label='teacher_chinese'
            ),
        })
        print(f"Saving tokenized datasets to {ds_save_path} ...")
        tokenized_datasets.save_to_disk(ds_save_path)


    del teacher_model, teacher_tokenizer
    torch.cuda.empty_cache()



    # 3. 加载学生模型
    student_model, student_tokenizer = load_model_and_tokenizer(
        is_teacher=False
    )

    # 4. 为学生模型预处理数据
    #remove_cols = distillation_datasets["train"].column_names
    # tokenized_datasets = distillation_datasets.map(
    #     lambda examples: preprocess_data(
    #         examples, tokenizer=student_tokenizer, label="teacher_chinese"
    #     ),
    #     batched=True,
    #     remove_columns=remove_cols,
    #     desc="Running tokenizer on dataset",
    # )

    
    # 5. 配置 LoRA 
    peft_config = LoraConfig(
        task_type=TaskType.CAUSAL_LM,
        r=LORA_R,
        lora_alpha=LORA_ALPHA,
        lora_dropout=LORA_DROPOUT,
        target_modules=LORA_TARGET_MODULES,
    )
    student_model = get_peft_model(student_model, peft_config)
    student_model.print_trainable_parameters()

    # 6. 训练学生模型
    print("--- Starting Student Model Training ---")
    train_student_model(student_model, student_tokenizer, tokenized_datasets)


if __name__ == "__main__":
    main()
    