from datasets import load_dataset, load_from_disk
import numpy as np
import matplotlib.pyplot as plt

# 加载本地数据集
dataset = load_dataset("wlhb/Transaltion-Chinese-2-English")['train'].select(range(60000))

# 定义一个函数来计算文本长度
def compute_text_length(example):
    return {'length': len(example['english'].split())}  # 以 token 为单位计算长度

# 将该函数应用到数据集
dataset = dataset.map(compute_text_length)

# 获取所有文本的长度
lengths = dataset['length']


max_length = np.max(lengths)
average_length = np.mean(lengths)
percentile_90 = np.percentile(lengths, 90)
percentile_95 = np.percentile(lengths, 95)
percentile_99 = np.percentile(lengths, 99)

print(f"Max length: {max_length}")
print(f"Average length: {average_length}")
print(f"90th percentile length: {percentile_90}")
print(f"95th percentile length: {percentile_95}")
print(f"99th percentile length: {percentile_99}")

plt.figure(figsize=(10, 6))
plt.hist(lengths, bins=50, alpha=0.7)
plt.axvline(x=percentile_95, color='r', linestyle='--', label='95th percentile')
plt.axvline(x=percentile_99, color='g', linestyle='--', label='99th percentile')
plt.xlabel('Text Length (words)')
plt.ylabel('Frequency')
plt.title('Distribution of Text Lengths')
plt.legend()
plt.savefig('text_length_distribution.png')
plt.show()
