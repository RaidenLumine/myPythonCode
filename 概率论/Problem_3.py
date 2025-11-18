import math
import sys

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# 设置样本的大小
default_size = 5000
default_n = 10000

# 使用均匀分布生成样本的随机数，生成default_n组，每组default_size个
u = np.random.rand(default_size, default_n)

# 将均匀分布的随机数转换为正态分布的样本
z = u.sum(axis=1)

# 绘制直方图
plt.hist(z, bins=50, density=True)

# 真实的正态分布的均值与标准差
mean = 1 / 2 * default_n
std = np.sqrt(default_n * (1 / 12))

# 绘制正态分布曲线
x = np.linspace(mean - 3 * std, mean + 3 * std, 100)
y = norm.pdf(x, mean, std)
plt.plot(x, y)

plt.show()


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


# 两点分布
p = 0.5
a = 0
b = 1

output = []  # 输出图像的数据数组

# 生成n组二项分布的样本
for i in range(default_size):
    binomial_samples = binomial(default_n, p)
    count = 0
    for j in range(default_n):
        if binomial_samples[j] == 1:
            count += 1
    output.append(count)

# 绘制直方图
plt.hist(output, bins=50, density=True)

# 真实的正态分布的均值与标准差
mean = default_n * p
std = np.sqrt(default_n * p * (1 - p))

# 绘制正态分布曲线
x = np.linspace(mean - 3 * std, mean + 3 * std, 100)
y = norm.pdf(x, mean, std)
plt.plot(x, y)

plt.show()

sys.exit(0)
