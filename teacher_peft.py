import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
import torch
from transformers import (
    AutoTokenizer,
    AutoModelForCausalLM,
    TrainingArguments,
    Trainer,
    DefaultDataCollator,
)
from datasets import DatasetDict
from peft import LoraConfig, get_peft_model, TaskType
import matplotlib.pyplot as plt
import evaluate

from data import load_and_prepare_dataset, preprocess_data
from eval import evaluate_model_generation
# --- 配置 ---
bertscore=evaluate.load("bertscore")

MODEL_PATH = "./models/Qwen2.5_1.5B_Instruct"
OUTPUT_DIR = "./teacher_lora"
LOGGING_DIR = "./teacher_lora/logs"

BATCH_SIZE = 1
LEARNING_RATE = 4e-4
NUM_EPOCHS = 3
LOGGING_STEPS = 50
WARMUP_RATIO=0.1
WEIGHT_DECAY=0.03
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


# --- 2. 加载数据集 ---
raw_datasets = load_and_prepare_dataset()


# --- 2. 加载 Tokenizer 和模型 ---
print("Loading tokenizer and model...")
tokenizer = AutoTokenizer.from_pretrained(
    MODEL_PATH, trust_remote_code=True, padding_side="left"
)
tokenizer.pad_token = tokenizer.eos_token
model = AutoModelForCausalLM.from_pretrained(
    MODEL_PATH,
    torch_dtype=torch.bfloat16,
    device_map="auto",
    trust_remote_code=True,
)
print("Model loaded.")


# --- 3. 预处理数据集 ---
print("Preprocessing dataset...")
tokenized_datasets = DatasetDict({
    "train": preprocess_data(
        raw_datasets["train"],tokenizer,label='chinese'
    ),
    "eval": preprocess_data(
        raw_datasets["eval"],tokenizer,label='chinese'
    ),
})


# --- 4. 配置 LoRA ---
peft_config = LoraConfig(
    task_type=TaskType.CAUSAL_LM,
    r=LORA_R,
    lora_alpha=LORA_ALPHA,
    lora_dropout=LORA_DROPOUT,
    target_modules=LORA_TARGET_MODULES,
)

model = get_peft_model(model, peft_config)
model.cuda()


# --- 5. 定义训练参数 ---
print("Setting up training arguments...")
training_args = TrainingArguments(
    output_dir=OUTPUT_DIR,
    per_device_train_batch_size=BATCH_SIZE,
    per_device_eval_batch_size=BATCH_SIZE,
    learning_rate=LEARNING_RATE,
    num_train_epochs=NUM_EPOCHS,
    logging_dir=LOGGING_DIR,
    logging_steps=LOGGING_STEPS,
    eval_strategy="epoch",
    save_strategy="epoch",
    bf16=True,
    warmup_ratio=WARMUP_RATIO,
    metric_for_best_model="eval_loss",
    greater_is_better=False,
    label_names=["labels"],
    lr_scheduler_type="cosine",
    weight_decay=WEIGHT_DECAY,
)


# --- 7. 实例化 Trainer ---
print("Initializing Trainer...")
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_datasets["train"],
    eval_dataset=tokenized_datasets["eval"],
    data_collator=DefaultDataCollator(),
    tokenizer=tokenizer,
)


# --- 8. 开始训练 ---
print("Starting training...")
train_result = trainer.train()
print("Training finished.")


# --- 9. 保存模型和指标 ---
print("Saving final LoRA adapter...")
# 保存 LoRA adapter 和 tokenizer
model.save_pretrained(OUTPUT_DIR) # 或者如果只想保存 adapter
tokenizer.save_pretrained(OUTPUT_DIR) # Tokenizer 也应保存

# 保存训练指标
metrics = train_result.metrics
trainer.log_metrics("train", metrics)
trainer.save_metrics("train", metrics)
trainer.save_state()

# 绘制损失曲线
training_logs = [
    log for log in trainer.state.log_history if "step" in log and "loss" in log and 'eval_loss' not in log # 过滤掉评估日志
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


# --- 10. 评估模型 ---
print("\n--- Evaluating using model.generate() ---")

model.eval()
model.to('cuda')

eval_dataset = tokenized_datasets["eval"]
all_preds = []
all_labels = []

generation_config = {
    "pad_token_id": tokenizer.pad_token_id,
    "eos_token_id": tokenizer.eos_token_id,
    "do_sample": False, 
    "temperature":None,
    "top_k":None,
    "top_p":None,
}

bertscore_results_gen = evaluate_model_generation(
    model=trainer.model, 
    tokenizer=tokenizer,
    eval_dataset=tokenized_datasets["eval"],
    generation_config=generation_config,
    bertscore_metric=bertscore,
    device=training_args.device 
)

print("Script finished successfully!")
print(f"Model/Adapter saved to: {OUTPUT_DIR}")


#os.system("shutdown /s /t 1")
plt.show()