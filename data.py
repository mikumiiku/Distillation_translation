'''
数据集相关设置和函数
'''
from datasets import load_dataset, DatasetDict,Dataset
PATH='wmt/wmt19','zh-en'

TRAIN_SIZE=2000
EVAL_SIZE=400
USE_SMALL_SUBSET=False
SMALL_TRAIN_SIZE=20
SMALL_EVAL_SIZE=5

MAX_INPUT_LENGTH=256
MAX_TARGET_LENGTH=256
MAX_SEQ_LENGTH=MAX_INPUT_LENGTH+MAX_TARGET_LENGTH

PROMPT_TEMPLATE = (
    "<|im_start|>system\nYou are a helpful assistant that translates english documents to chinese documents.<|im_end|>\n"
    "<|im_start|>user\nTranslate the following english document to chinese document without any explaination:\n{eng}\n<|im_end|>\n"
    "<|im_start|>assistant\n"
)



def load_and_prepare_dataset():
    """加载DataDict并准备训练/评估子集。"""
    full_ds = load_dataset(PATH[0],PATH[1])['train']

    train_size = SMALL_TRAIN_SIZE if USE_SMALL_SUBSET else TRAIN_SIZE
    eval_size = SMALL_EVAL_SIZE if USE_SMALL_SUBSET else EVAL_SIZE

    train_subset = full_ds.select(range(train_size))
    eval_subset = full_ds.select(range(train_size,train_size+eval_size))

    raw_ds = DatasetDict({"train": train_subset, "eval": eval_subset}).map(
        lambda x: {'english': x['translation']['en'],'chinese': x['translation']['zh']},
        remove_columns='translation'
    )

    return raw_ds

def preprocess_data(examples:Dataset, tokenizer,label):
    '''加载Dataset生成model_inputs = {"input_ids", "attention_mask", "labels"}'''
    prompts = [PROMPT_TEMPLATE.format(eng=eng) for eng in examples["english"]]
    targets = [
        str(translation) + tokenizer.eos_token for translation in examples[label]
    ]

    model_inputs = {"input_ids": [], "attention_mask": [], "labels": []}

    for prompt, target in zip(prompts, targets):
        tokenized_prompt = tokenizer(
            prompt,
            truncation=True,
            max_length=MAX_INPUT_LENGTH,
            add_special_tokens=False,
        )
        tokenized_target = tokenizer(
            target,
            truncation=True,
            max_length=MAX_TARGET_LENGTH,
            add_special_tokens=False,
        )

        prompt_ids = tokenized_prompt["input_ids"]
        target_ids = tokenized_target["input_ids"]

        input_ids = prompt_ids + target_ids
        attention_mask = [1] * len(input_ids)
        labels = [-100] * len(prompt_ids) + target_ids

        padding_length = MAX_SEQ_LENGTH - len(input_ids)

        if padding_length >= 0:
            input_ids += [tokenizer.pad_token_id] * padding_length
            attention_mask += [0] * padding_length
            labels += [-100] * padding_length
        else:
            input_ids = input_ids[: MAX_SEQ_LENGTH]
            attention_mask = attention_mask[: MAX_SEQ_LENGTH]
            labels = labels[: MAX_SEQ_LENGTH]
            if labels[-1] != -100:
                input_ids[-1] = tokenizer.eos_token_id
                labels[-1] = tokenizer.eos_token_id

        model_inputs["input_ids"].append(input_ids)
        model_inputs["attention_mask"].append(attention_mask)
        model_inputs["labels"].append(labels)

    return Dataset.from_dict(model_inputs)


def load_test_dataset(TEST_SIZE):
    full_ds = load_dataset(PATH[0],PATH[1])['validation']
    full_ds = full_ds.map(lambda x: {
        'english': x['translation']['en'],
        'chinese': x['translation']['zh']
    })
    ds = full_ds.select(range(TEST_SIZE))
    return ds
