"""
将在Xsum上微调过的Qwen2.5-1.5B-Instruct通过硬标签蒸馏方式蒸馏到Qwen2.5-0.5B-Instruct
"""
import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
import torch
from datasets import DatasetDict
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    Seq2SeqTrainingArguments,
    Seq2SeqTrainer,
    DataCollatorForLanguageModeling,
    EarlyStoppingCallback,
)
import matplotlib.pyplot as plt
import torch.nn.functional as F
from data import load_and_prepare_dataset, preprocess_data
from peft import PeftModel, LoraConfig, get_peft_model, TaskType

device = torch.device("cuda")
TEACHER_MODEL_NAME = "Qwen/Qwen2.5-1.5B-Instruct"
TEACHER_MODEL_PATH = "./models/Qwen2.5_1.5B_Instruct"
STUDENT_MODEL_NAME = "Qwen/Qwen2.5-0.5B-Instruct"
STUDENT_MODEL_PATH = "./models/Qwen2.5_0.5B_Instruct"
LORA_PATH='./teacher_lora'

OUTPUT_DIR = "./SLKD_lora"
LOGGING_DIR = "./SLKD_lora/logs"
NUM_TRAIN_EPOCHS = 3
TRAIN_BATCH_SIZE = 1
EVAL_BATCH_SIZE = 1
LEARNING_RATE = 4e-5
WEIGHT_DECAY = 0.03
WARMUP_RATIO = 0.1
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
# 蒸馏参数
TEMPERATURE = 2.0  # 蒸馏温度
ALPHA_CE = 0.5

PROMPT_TEMPLATE = (
    "<|im_start|>system\nYou are a helpful assistant that translates english documents to chinese documents.<|im_end|>\n"
    "<|im_start|>user\nTranslate the following english document to chinese document without any explaination:\n{eng}\n<|im_end|>\n"
    "<|im_start|>assistant\n"
)



class WBKDTrainer(Seq2SeqTrainer):
    """
    自定义 Trainer，用于实现知识蒸馏（软标签）。
    """

    def __init__(
        self, *args, teacher_model=None, temperature=2.0, alpha_ce=0.5, **kwargs
    ):
        super().__init__(*args, **kwargs)
        self.teacher_model = teacher_model
        self.temperature = temperature
        self.alpha_ce = alpha_ce
        if self.teacher_model is not None:
            self.teacher_model.eval()
            self.teacher_model.requires_grad_(False)

    def compute_loss(self, model, inputs, return_outputs=False, **kwargs):
        """
        计算包含标准交叉熵损失和 KL 散度蒸馏损失的总损失。
        """
        # --- 学生模型前向传播 ---
        student_outputs = model(**inputs)
        student_logits = student_outputs.logits
        labels = inputs.get("labels")
        shifted_student_logits = student_logits[..., :-1, :].contiguous()
        shifted_labels = labels[..., 1:].contiguous()

        loss_fct = torch.nn.CrossEntropyLoss(ignore_index=-100)
        loss_ce = loss_fct(
            shifted_student_logits.view(-1, shifted_student_logits.size(-1)),
            shifted_labels.view(-1),
        )

        # --- 蒸馏损失---
        loss_kl = 0.0
        if self.teacher_model is not None and self.alpha_ce < 1.0:
            # --- 教师模型前向传播 ---
            with torch.no_grad():
                teacher_outputs = self.teacher_model(**inputs)
                teacher_logits = teacher_outputs.logits

            # 同样需要移动教师模型的 logits
            shifted_teacher_logits = teacher_logits[..., :-1, :].contiguous()

            # --- 计算 KL 散度损失 ---
            # 应用温度进行 Softmax
            soft_student_log_probs = F.log_softmax(
                shifted_student_logits / self.temperature, dim=-1
            )
            soft_teacher_probs = F.softmax(
                shifted_teacher_logits / self.temperature, dim=-1
            )

            # 计算 KL 散度。`log_target=False` 因为 teacher_probs 已经是概率
            # reduction='none' 以便我们可以应用 mask
            kl_div_element_wise = F.kl_div(
                soft_student_log_probs,
                soft_teacher_probs,
                reduction="none",
                log_target=False,
            ).sum(
                dim=-1
            )  # 形状: (batch_size, seq_len - 1)

            # 创建 mask 以忽略填充位置 (标签为 -100)
            mask = (shifted_labels != -100).float()

            # 应用 mask 并计算平均 KL 散度损失 (仅在非填充位置)
            # 乘以 T*T 是 KL 散度蒸馏的标准做法
            loss_kl = (
                (kl_div_element_wise * mask).sum() / mask.sum() * (self.temperature**2)
            )

        # --- 3. 组合损失 ---
        # loss = alpha * CE_loss + (1 - alpha) * KL_loss
        loss = self.alpha_ce * loss_ce + (1.0 - self.alpha_ce) * loss_kl

        return (loss, student_outputs) if return_outputs else loss


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


def train_student_model(
    student_model,
    student_tokenizer,
    teacher_model,
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
        remove_unused_columns=False,
    )

    data_collator = DataCollatorForLanguageModeling(
        tokenizer=student_tokenizer, mlm=False
    )

    trainer = WBKDTrainer(
        model=student_model,
        args=training_args,
        train_dataset=tokenized_datasets["train"],
        eval_dataset=tokenized_datasets["eval"],
        data_collator=data_collator,
        callbacks=[EarlyStoppingCallback(early_stopping_patience=3)],
        teacher_model=teacher_model,
        temperature=TEMPERATURE,
        alpha_ce=ALPHA_CE,
    )

    train_result = trainer.train()

    trainer.save_model()
    trainer.log_metrics("train", train_result.metrics)
    trainer.save_metrics("train", train_result.metrics)
    trainer.save_state()

    training_logs = [
        log for log in trainer.state.log_history if "step" in log and "loss" in log
    ]
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
    #plt.show()

    eval_metrics = trainer.evaluate()
    trainer.log_metrics("eval", eval_metrics)
    trainer.save_metrics("eval", eval_metrics)

    # Clean up GPU memory after training
    del student_model, teacher_model, trainer, data_collator
    torch.cuda.empty_cache()


def main():

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # 1. 加载和准备数据集
    raw_datasets = load_and_prepare_dataset()
    distillation_datasets = DatasetDict(
        {"train": raw_datasets["train"], "eval": raw_datasets["eval"]}
    )


    # 2. 加载学生模型
    student_model, student_tokenizer = load_model_and_tokenizer(is_teacher=False)
    print("student loaded.")

    # 3. 为学生模型预处理数据
    tokenized_datasets = DatasetDict({
        "train": preprocess_data(
            raw_datasets["train"],student_tokenizer,label='chinese'
        ),
        "eval": preprocess_data(
            raw_datasets["eval"],student_tokenizer,label='chinese'
        ),
    })
    # 4. 配置 LoRA
    peft_config = LoraConfig(
        task_type=TaskType.CAUSAL_LM,
        r=LORA_R,
        lora_alpha=LORA_ALPHA,
        lora_dropout=LORA_DROPOUT,
        target_modules=LORA_TARGET_MODULES,
    )
    student_model = get_peft_model(student_model, peft_config)
    student_model.print_trainable_parameters()

    # 5. 加载教师模型
    teacher_model, teacher_tokenizer = load_model_and_tokenizer(
        is_teacher=True
    )
    print("teacher loaded.")

    # 6. 训练学生模型
    print("--- Starting Student Model Training ---")
    train_student_model(
        student_model, student_tokenizer, teacher_model, tokenized_datasets
    )
    os.system("shutdown /s /t 1")


if __name__ == "__main__":
    main()
