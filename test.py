import torch
from datasets import load_dataset
from transformers import (
    AutoTokenizer,
    AutoModelForCausalLM,
    pipeline
)
import evaluate
from tqdm import tqdm
from peft import PeftModel
import numpy as np
from data import load_test_dataset

# --- Configuration ---
metrics = evaluate.load('bertscore')

MODEL_PATHS = {
    "TEACHER": "./models/Qwen2.5_1.5B_Instruct",
    "STUDENT": "./models/Qwen2.5_0.5B_Instruct",
    "TEACHER_PEFT": "./teacher_lora",
    "STUDENT_PEFT": "./student_lora",
    "HLKD": "./HLKD_lora",
    "SLKD": "./SLKD_lora",
}
BASE_MODEL_MAPPING = {
    "STUDENT_PEFT": "STUDENT",
    "TEACHER_PEFT": "TEACHER",
    "HLKD": "STUDENT",
    "SLKD": "STUDENT", 
}

TEST_SIZE = 20
OUTPUT_FILE = "TEST_BERTSCORE.md"
MAX_NEW_TOKENS = 400
DEVICE = "cuda"
TORCH_DTYPE = torch.bfloat16

PROMPT_TEMPLATE = (
    "<|im_start|>system\nYou are a helpful assistant that translates english documents to chinese documents.<|im_end|>\n"
    "<|im_start|>user\nTranslate the following english document to chinese document without any explaination:\n{eng}\n<|im_end|>\n"
    "<|im_start|>assistant\n"
)

# --- Load Data ---
dataset=load_test_dataset(TEST_SIZE)

# --- Prepare Evaluation Structure ---
eval_results = []
for i in range(len(dataset)):
    eval_results.append({
        "english": dataset[i]["english"],
        "reference_chinese": dataset[i]["chinese"],
        "model_outputs": {} 
    })

model_avg_scores = {}

# --- Model Evaluation Loop ---
for model_name, model_or_adapter_path in MODEL_PATHS.items():
    print(f"\n--- Testing model: {model_name} ---")
    model = None
    pipe = None
    base_model_path = None

    # Determine base model path
    is_peft = model_name in BASE_MODEL_MAPPING
    if is_peft:
        base_model_key = BASE_MODEL_MAPPING.get(model_name)
        base_model_path = MODEL_PATHS[base_model_key]
        adapter_path = model_or_adapter_path
        print(f"PEFT Model: Using base {base_model_path} and adapter {adapter_path}")
    else:
        base_model_path = model_or_adapter_path
        adapter_path = None
        print(f"Base Model: {base_model_path}")

    # --- Load Model ---
    print(f"Loading model from: {base_model_path}")
    model = AutoModelForCausalLM.from_pretrained(
        base_model_path,
        torch_dtype=TORCH_DTYPE,
        trust_remote_code=True
    )

    if is_peft and adapter_path:
        print(f"Loading adapter from: {adapter_path}")
        model = PeftModel.from_pretrained(model, adapter_path)
        model = model.merge_and_unload()
    print("Model loaded.")
        
    # --- Create Pipeline ---
    print("Creating text-generation pipeline...")
    pipe = pipeline(
        "text-generation",
        model=model,
        tokenizer = AutoTokenizer.from_pretrained(base_model_path, trust_remote_code=True, padding_side="left"),
        torch_dtype=TORCH_DTYPE,
        device="cuda", 
        trust_remote_code=True,
        max_new_tokens=MAX_NEW_TOKENS,
    )
    print("Pipeline created.")

    # --- Generate Translations ---
    print(f"Generating translations for {model_name}...")
    prompts = [PROMPT_TEMPLATE.format(eng=sample["english"]) for sample in dataset]

    generated_outputs = pipe(
        prompts,
        batch_size=4 # Adjust based on GPU memory
    )
    predictions = []
    for i, output in tqdm(enumerate(generated_outputs), total=len(prompts), desc=f"Processing ({model_name})"):
        full_text = output[0]['generated_text']
        assistant_tag = "<|im_start|>assistant\n"
        assistant_pos = full_text.rfind(assistant_tag)
        generated_translation = full_text[assistant_pos + len(assistant_tag):]
        predictions.append(generated_translation)
        eval_results[i]["model_outputs"][model_name] = generated_translation

    # --- Calculate and Store Scores for this Model ---
    print(f"Calculating scores for {model_name}...")
    references = [res["reference_chinese"] for res in eval_results]
    metric_output =metrics.compute(predictions=predictions, references=references,lang='zh')
    model_avg_scores[model_name] = metric_output
    print(f"Average score for {model_name}: {metric_output}")

    # --- Clean up ---
    del model
    del pipe
    torch.cuda.empty_cache()
    print(f"Finished evaluating {model_name}.")


# --- Save Results ---
print(f"Saving results to {OUTPUT_FILE}...")
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write("# Translation Evaluation Results\n\n")

    f.write("## Individual Sample Results\n\n")
    for i, result in enumerate(eval_results):
        f.write(f"### Sample {i+1}\n\n")
        f.write(f"**English:**\n```\n{result['english']}\n```\n\n")
        f.write(f"**Reference Chinese:**\n```\n{result['reference_chinese']}\n```\n\n")
        f.write("**Model Outputs:**\n")
        for model_name, output in result['model_outputs'].items():
            f.write(f"*   **{model_name}:**\n    ```\n    {output}\n    ```\n")
        f.write("\n---\n\n")

    f.write("## Overall Model Scores (BERTScore)\n\n")
    for model_name, scores in model_avg_scores.items():
        f.write(f"### {model_name}\n")
        f.write(f"*   **Average F1:** {np.mean(scores['f1']):.4f}\n")
        f.write(f"*   **Average Precision:** {np.mean(scores['precision']):.4f}\n")
        f.write(f"*   **Average Recall:** {np.mean(scores['recall']):.4f}\n\n")

print(f"Results saved to {OUTPUT_FILE}.")

