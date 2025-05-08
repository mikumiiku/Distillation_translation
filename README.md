# README.md
<!-- filepath: README.md -->
# 基于知识蒸馏的英汉翻译模型压缩

本项目旨在探索将大型预训练语言模型（教师模型）的知识迁移到较小模型（学生模型）的技术，特别是在英汉翻译任务上。我们使用了 Qwen2.5 系列模型，并比较了不同的微调和知识蒸馏方法。

## 模型

*   **教师模型 (Teacher):** [`./models/Qwen2.5_1.5B_Instruct`](./models/Qwen2.5_1.5B_Instruct) (基础模型)
*   **学生模型 (Student):** [`./models/Qwen2.5_0.5B_Instruct`](./models/Qwen2.5_0.5B_Instruct) (基础模型)
*   **教师模型 PEFT (Teacher_PEFT):** 使用 LoRA 在翻译任务上微调的教师模型 ([`teacher_peft.py`](teacher_peft.py), 适配器保存在 [`./teacher_lora/`](./teacher_lora/))
*   **学生模型 PEFT (Student_PEFT):** 使用 LoRA 在翻译任务上微调的学生模型 ([`student_peft.py`](student_peft.py), 适配器保存在 [`./student_lora/`](./student_lora/))
*   **硬标签知识蒸馏 (HLKD):** 使用 Teacher_PEFT 生成的译文作为硬标签，通过 LoRA 训练学生模型 ([`HLKD.py`](HLKD.py), 适配器保存在 [`./HLKD_lora/`](./HLKD_lora/))
*   **软标签知识蒸馏 (SLKD):** 结合 Teacher_PEFT 的 logits 输出（软标签）和真实标签，通过 LoRA 训练学生模型 ([`SLKD.py`](SLKD.py), 适配器保存在 [`./SLKD_lora/`](./SLKD_lora/))

## 评估

我们使用 [BERTScore](https://huggingface.co/spaces/evaluate-metric/bertscore) 来评估模型在测试集上的翻译质量。评估脚本为 [`test.py`](test.py)。

### 最终评估结果 (BERTScore)

结果来自 [TEST_BERTSCORE.md](TEST_BERTSCORE.md):

| 模型           | 平均 F1 | 平均 Precision | 平均 Recall |
| -------------- | -------- | ------------- | ---------- |
| TEACHER        | 0.8181   | 0.8214        | 0.8161     |
| STUDENT        | 0.7812   | 0.7862        | 0.7775     |
| TEACHER_PEFT   | 0.8290   | 0.8272        | 0.8318     |
| STUDENT_PEFT   | 0.7910   | 0.7986        | 0.7844     |
| **HLKD**       | 0.7918   | 0.7944        | 0.7900     |
| **SLKD**       | 0.7720   | 0.7869        | 0.7594     |

## 蒸馏方法比较

本项目比较了两种主要的知识蒸馏方法：

1.  **硬标签知识蒸馏 (HLKD - Hard Label Knowledge Distillation):**
    *   **原理:** 首先使用教师模型 ([`Teacher_PEFT`](./teacher_lora/)) 对训练集中的英文文本生成中文译文（硬标签）。然后，将这些生成的译文作为目标，训练学生模型。
    *   **实现:** 见 [`HLKD.py`](HLKD.py)。
    *   **优点:** 实现相对简单，训练学生时不需要加载教师模型，内存开销较小。
    *   **缺点:** 教师模型生成的硬标签可能包含噪声或错误。丢失了教师模型预测的概率分布信息（软知识）。
    *   **结果:** 在本次实验中，HLKD (F1: 0.7918) 的表现略优于直接微调的学生模型 (Student_PEFT F1: 0.7910)，并且显著优于 SLKD。

2.  **软标签知识蒸馏 (SLKD - Soft Label Knowledge Distillation):**
    *   **原理:** 在训练学生模型时，不仅使用真实的标签（Ground Truth）计算交叉熵损失，还引入教师模型的输出 logits。通过计算学生模型 logits 和教师模型 logits 之间的 KL 散度，引导学生模型模仿教师模型的预测分布。通常使用温度（Temperature）来平滑概率分布。损失函数通常是 `alpha * CE_loss + (1 - alpha) * KL_loss`。
    *   **实现:** 见 [`SLKD.py`](SLKD.py) 中的自定义 `WBKDTrainer`。
    *   **优点:** 能够传递更丰富的知识，包括教师模型对于不同预测的“置信度”或不确定性，理论上可能获得更好的性能。
    *   **缺点:** 实现更复杂，需要在训练学生时同时加载教师模型，计算 KL 散度，导致更高的计算和内存开销。对超参数（如温度 `TEMPERATURE`、损失权重 `ALPHA_CE`）更敏感。
    *   **结果:** 在本次实验中，SLKD (F1: 0.7720) 的表现不如 HLKD，甚至略低于基础的学生模型 (STUDENT F1: 0.7812)。这可能归因于超参数设置不优、实现细节或任务特性。尽管理论上 SLKD 能传递更多信息，但实际效果需要仔细调优。

**结论:** 在当前设置下，HLKD 方法在性能和实现复杂度之间取得了较好的平衡，其结果略微超过了直接对学生模型进行 PEFT 微调。SLKD 的表现不佳，提示需要进一步调整超参数或检查实现。

## 未来工作：消融实验

为了更深入地理解不同因素对蒸馏效果的影响，计划进行以下消融实验：

1.  **SLKD 超参数调整:**
    *   **蒸馏温度 (Temperature):** 测试 [`SLKD.py`](SLKD.py) 中不同的 `TEMPERATURE` 值（例如 1.0, 1.5, 2.5, 3.0），观察其对 KL 散度损失和最终性能的影响。
    *   **损失权重 (Alpha CE):** 调整 [`SLKD.py`](SLKD.py) 中的 `ALPHA_CE`（例如 0.1, 0.3, 0.7, 0.9），改变交叉熵损失和 KL 散度损失的相对重要性。

2.  **LoRA 超参数调整:**
    *   在 [`HLKD.py`](HLKD.py) 和 [`SLKD.py`](SLKD.py) 中，尝试不同的 LoRA 配置（`LORA_R`, `LORA_ALPHA`, `LORA_DROPOUT`），并与 [`student_peft.py`](student_peft.py) 的结果进行比较，以确定蒸馏过程中的最佳 LoRA 设置。

3.  **教师模型选择:**
    *   比较使用基础 Teacher 模型 ([`./models/Qwen2.5_1.5B_Instruct`](./models/Qwen2.5_1.5B_Instruct)) 与微调后的 Teacher_PEFT 模型 ([`./teacher_lora/`](./teacher_lora/)) 作为蒸馏过程中的教师，对 HLKD 和 SLKD 结果的影响。

4.  **HLKD 生成参数:**
    *   研究 [`HLKD.py`](HLKD.py) 中教师模型生成硬标签时使用的解码参数（如 `num_beams`, `temperature`, `top_k`, `top_p`）对最终学生模型性能的影响。

5.  **数据规模:**
    *   通过调整 [`data.py`](data.py) 中的 `TRAIN_SIZE` 和 `EVAL_SIZE`，评估训练数据量对蒸馏效果的影响。

## 环境设置与运行

1.  **创建 Conda 环境:**
    ```bash
    conda env create -f environment.yaml
    conda activate distillation
    ```
2.  **下载模型:** (如果尚未下载)
    *   需要将 Qwen2.5-1.5B-Instruct 和 Qwen2.5-0.5B-Instruct 模型文件分别放置在 `./models/Qwen2.5_1.5B_Instruct` 和 `./models/Qwen2.5_0.5B_Instruct` 目录下。
3.  **运行训练脚本:**
    *   微调教师模型: `python teacher_peft.py`
    *   微调学生模型: `python student_peft.py`
    *   运行 HLKD: `python HLKD.py`
    *   运行 SLKD: `python SLKD.py`
4.  **运行评估脚本:**
    *   `python test.py` (确保所有需要的模型/适配器已训练并保存在对应目录)

```# README.md
<!-- filepath: README.md -->
# 基于知识蒸馏的英汉翻译模型压缩

本项目旨在探索将大型预训练语言模型（教师模型）的知识迁移到较小模型（学生模型）的技术，特别是在英汉翻译任务上。我们使用了 Qwen2.5 系列模型，并比较了不同的微调和知识蒸馏方法。

## 模型

*   **教师模型 (Teacher):** [`./models/Qwen2.5_1.5B_Instruct`](./models/Qwen2.5_1.5B_Instruct) (基础模型)
*   **学生模型 (Student):** [`./models/Qwen2.5_0.5B_Instruct`](./models/Qwen2.5_0.5B_Instruct) (基础模型)
*   **教师模型 PEFT (Teacher_PEFT):** 使用 LoRA 在翻译任务上微调的教师模型 ([`teacher_peft.py`](teacher_peft.py), 适配器保存在 [`./teacher_lora/`](./teacher_lora/))
*   **学生模型 PEFT (Student_PEFT):** 使用 LoRA 在翻译任务上微调的学生模型 ([`student_peft.py`](student_peft.py), 适配器保存在 [`./student_lora/`](./student_lora/))
*   **硬标签知识蒸馏 (HLKD):** 使用 Teacher_PEFT 生成的译文作为硬标签，通过 LoRA 训练学生模型 ([`HLKD.py`](HLKD.py), 适配器保存在 [`./HLKD_lora/`](./HLKD_lora/))
*   **软标签知识蒸馏 (SLKD):** 结合 Teacher_PEFT 的 logits 输出（软标签）和真实标签，通过 LoRA 训练学生模型 ([`SLKD.py`](SLKD.py), 适配器保存在 [`./SLKD_lora/`](./SLKD_lora/))

## 评估

我们使用 [BERTScore](https://huggingface.co/spaces/evaluate-metric/bertscore) 来评估模型在测试集上的翻译质量。评估脚本为 [`test.py`](test.py)。

### 最终评估结果 (BERTScore)

结果来自 [TEST_BERTSCORE.md](TEST_BERTSCORE.md):

| 模型           | 平均 F1 | 平均 Precision | 平均 Recall |
| -------------- | -------- | ------------- | ---------- |
| TEACHER        | 0.8181   | 0.8214        | 0.8161     |
| STUDENT        | 0.7812   | 0.7862        | 0.7775     |
| TEACHER_PEFT   | 0.8290   | 0.8272        | 0.8318     |
| STUDENT_PEFT   | 0.7910   | 0.7986        | 0.7844     |
| **HLKD**       | 0.7918   | 0.7944        | 0.7900     |
| **SLKD**       | 0.7720   | 0.7869        | 0.7594     |

## 蒸馏方法比较

本项目比较了两种主要的知识蒸馏方法：

1.  **硬标签知识蒸馏 (HLKD - Hard Label Knowledge Distillation):**
    *   **原理:** 首先使用教师模型 ([`Teacher_PEFT`](./teacher_lora/)) 对训练集中的英文文本生成中文译文（硬标签）。然后，将这些生成的译文作为目标，训练学生模型。
    *   **实现:** 见 [`HLKD.py`](HLKD.py)。
    *   **优点:** 实现相对简单，训练学生时不需要加载教师模型，内存开销较小。
    *   **缺点:** 教师模型生成的硬标签可能包含噪声或错误。丢失了教师模型预测的概率分布信息（软知识）。
    *   **结果:** 在本次实验中，HLKD (F1: 0.7918) 的表现略优于直接微调的学生模型 (Student_PEFT F1: 0.7910)，并且显著优于 SLKD。

2.  **软标签知识蒸馏 (SLKD - Soft Label Knowledge Distillation):**
    *   **原理:** 在训练学生模型时，不仅使用真实的标签（Ground Truth）计算交叉熵损失，还引入教师模型的输出 logits。通过计算学生模型 logits 和教师模型 logits 之间的 KL 散度，引导学生模型模仿教师模型的预测分布。通常使用温度（Temperature）来平滑概率分布。损失函数通常是 `alpha * CE_loss + (1 - alpha) * KL_loss`。
    *   **实现:** 见 [`SLKD.py`](SLKD.py) 中的自定义 `WBKDTrainer`。
    *   **优点:** 能够传递更丰富的知识，包括教师模型对于不同预测的“置信度”或不确定性，理论上可能获得更好的性能。
    *   **缺点:** 实现更复杂，需要在训练学生时同时加载教师模型，计算 KL 散度，导致更高的计算和内存开销。对超参数（如温度 `TEMPERATURE`、损失权重 `ALPHA_CE`）更敏感。
    *   **结果:** 在本次实验中，SLKD (F1: 0.7720) 的表现不如 HLKD，甚至略低于基础的学生模型 (STUDENT F1: 0.7812)。这可能归因于超参数设置不优、实现细节或任务特性。尽管理论上 SLKD 能传递更多信息，但实际效果需要仔细调优。

**结论:** 在当前设置下，HLKD 方法在性能和实现复杂度之间取得了较好的平衡，其结果略微超过了直接对学生模型进行 PEFT 微调。SLKD 的表现不佳，提示需要进一步调整超参数或检查实现。

## 未来工作：消融实验

为了更深入地理解不同因素对蒸馏效果的影响，计划进行以下消融实验：

1.  **SLKD 超参数调整:**
    *   **蒸馏温度 (Temperature):** 测试 [`SLKD.py`](SLKD.py) 中不同的 `TEMPERATURE` 值（例如 1.0, 1.5, 2.5, 3.0），观察其对 KL 散度损失和最终性能的影响。
    *   **损失权重 (Alpha CE):** 调整 [`SLKD.py`](SLKD.py) 中的 `ALPHA_CE`（例如 0.1, 0.3, 0.7, 0.9），改变交叉熵损失和 KL 散度损失的相对重要性。

2.  **LoRA 超参数调整:**
    *   在 [`HLKD.py`](HLKD.py) 和 [`SLKD.py`](SLKD.py) 中，尝试不同的 LoRA 配置（`LORA_R`, `LORA_ALPHA`, `LORA_DROPOUT`），并与 [`student_peft.py`](student_peft.py) 的结果进行比较，以确定蒸馏过程中的最佳 LoRA 设置。

3.  **教师模型选择:**
    *   比较使用基础 Teacher 模型 ([`./models/Qwen2.5_1.5B_Instruct`](./models/Qwen2.5_1.5B_Instruct)) 与微调后的 Teacher_PEFT 模型 ([`./teacher_lora/`](./teacher_lora/)) 作为蒸馏过程中的教师，对 HLKD 和 SLKD 结果的影响。

4.  **HLKD 生成参数:**
    *   研究 [`HLKD.py`](HLKD.py) 中教师模型生成硬标签时使用的解码参数（如 `num_beams`, `temperature`, `top_k`, `top_p`）对最终学生模型性能的影响。

5.  **数据规模:**
    *   通过调整 [`data.py`](data.py) 中的 `TRAIN_SIZE` 和 `EVAL_SIZE`，评估训练数据量对蒸馏效果的影响。

## 环境设置与运行

1.  **创建 Conda 环境:**
    ```bash
    conda env create -f environment.yaml
    conda activate distillation
    ```
2.  **下载模型:** (如果尚未下载)
    *   需要将 Qwen2.5-1.5B-Instruct 和 Qwen2.5-0.5B-Instruct 模型文件分别放置在 `./models/Qwen2.5_1.5B_Instruct` 和 `./models/Qwen2.5_0.5B_Instruct` 目录下。
3.  **运行训练脚本:**
    *   微调教师模型: `python teacher_peft.py`
    *   微调学生模型: `python student_peft.py`
    *   运行 HLKD: `python HLKD.py`
    *   运行 SLKD: `python SLKD.py`
4.  **运行评估脚本:**
    *   `python test.py` (确保所有需要的模型/适配器已训练并保存在对应目录)
