import sys

import numpy as np
import matplotlib.pyplot as plt

default_size = 10  # 每组的实验次数
default_n = 10000  # 重复多少组
default_p = 0.5  # 概率


def binomial(n, p):
    # n: 二项分布的总次数
    # p: 二项分布中每次成功的概率
    # 返回: 二项分布样本
    samples = []
    for i in range(n):
        # 生成一个均匀分布的随机数
        u = np.random.rand()
        # 如果随机数小于p，就认为是成功
        if u < p:
            samples.append(1)
        else:
            samples.append(0)
    return samples


output = []  # 输出图像的数据数组

# 生成n组二项分布的样本
for i in range(default_n):
    binomial_samples = binomial(default_size, default_p)
    count = 0
    for j in range(default_size):
        if binomial_samples[j] == 1:
            count += 1
    output.append(count)

# 画出二项分布样本的直方图
plt.rcParams['font.sans-serif'] = ['SimHei']  # 正常显示中文
plt.rcParams['axes.unicode_minus'] = False
plt.hist(output, bins=10, rwidth=1, color="orange")
plt.title('二项分布样本直方图')
plt.xlabel('成功次数')
plt.ylabel('组数')
plt.show()

sys.exit(0)