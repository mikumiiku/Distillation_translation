import torch
import numpy as np
from tqdm import tqdm

def evaluate_model_generation(model, tokenizer, eval_dataset, generation_config, bertscore_metric, device='cuda'):
    print("\n--- Evaluating using model.generate() ---")
    model.eval()
    model.to(device)

    all_preds = []
    all_labels = []

    print(f"Starting generation for {len(eval_dataset)} evaluation examples...")
    with torch.no_grad():
        for example in tqdm(eval_dataset, desc="Generating Eval Predictions"):
            input_ids_list = example['input_ids']
            labels_list = example['labels']

            prompt_end_index = next(i for i, label in enumerate(labels_list) if label != -100)

            prompt_ids = input_ids_list[:prompt_end_index]

            input_ids_tensor = torch.tensor([prompt_ids]).to(device)
            attention_mask_tensor = torch.ones_like(input_ids_tensor)

            generated_ids = model.generate(
                input_ids=input_ids_tensor,
                attention_mask=attention_mask_tensor,
                **generation_config
            )

            decoded_prediction = tokenizer.decode(
                generated_ids[0][len(prompt_ids):],
                skip_special_tokens=True
            )

            reference_ids = [label for label in labels_list[prompt_end_index:] if label != -100 and label != tokenizer.pad_token_id]
            decoded_label = tokenizer.decode(reference_ids, skip_special_tokens=True)

            all_preds.append(decoded_prediction.strip())
            all_labels.append(decoded_label.strip())

    print("\nCalculating BERTScore based on model.generate()...")

    bertscore_results = bertscore_metric.compute(
        predictions=all_preds,
        references=all_labels,
        lang="zh" 
    )

    print("\n--- BERTScore Results (using generate) ---")
    avg_precision = np.mean(bertscore_results.get('precision', [0.0]))
    avg_recall = np.mean(bertscore_results.get('recall', [0.0]))
    avg_f1 = np.mean(bertscore_results.get('f1', [0.0]))
    print(f"Precision: {avg_precision:.4f}")
    print(f"Recall:    {avg_recall:.4f}")
    print(f"F1 Score:  {avg_f1:.4f}")
    print("------------------------------------------")

    return bertscore_results