# 方法1： 中心极限定理
import sys

import numpy as np
from matplotlib import pyplot as plt

# 设置样本的大小
default_size = 5000
default_n = 10000

# 使用均匀分布生成随机数，生成default_size组，每组default_n个
u = np.random.rand(default_size, default_n)

# 将均匀分布的随机数转换为正态分布的样本
z = u.sum(axis=1) - default_n * 0.5  # 使图像居中

# 输出图像
plt.hist(z, bins=50, color="orange")
plt.show()

# 方法2：Box–Muller算法
# 使用numpy的均匀分布函数生成随机数
x = np.random.rand(10000)
y = np.random.rand(10000)

# 将均匀分布的随机数转换为正态分布的样本
z1 = np.sqrt(-2 * np.log(x)) * np.cos(2 * np.pi * y)

# 输出图像
plt.hist(z1, bins=50, color="orange")
plt.show()

sys.exit(0)