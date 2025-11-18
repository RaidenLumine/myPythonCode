import sys

import numpy as np
from matplotlib import pyplot as plt


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


# 设置样本容量
sample_sizes = np.linspace(1, 10000, 10000)

# 生成均匀分布样本
j_array = np.random.rand(10000)

# 生成两点分布样本
l_array = binomial(10000, 0.5)

# 生成正态分布样本
# 使用numpy的均匀分布函数生成随机数
x = np.random.rand(10000)
y = np.random.rand(10000)

# 将均匀分布的随机数转换为正态分布的样本
z_array = np.sqrt(-2 * np.log(x)) * np.cos(2 * np.pi * y) + 0.5

j_mean = []
l_mean = []
z_mean = []

for size in sample_sizes:
    # 计算随机变量的算术平均值
    j = np.mean(j_array[0:int(size)])
    j_mean.append(j)

    l = sum(l_array[0:int(size)]) / size
    l_mean.append(l)

    z = np.mean(z_array[0:int(size)])
    z_mean.append(z)

plt.ylim(0.4, 0.6)
plt.plot([0,10000],[0.5,0.5] ,color='black',linewidth=3)
plt.plot(j_mean, color='r')
plt.plot(l_mean, color='b')
plt.plot(z_mean, color='y')
plt.show()

sys.exit(0)
