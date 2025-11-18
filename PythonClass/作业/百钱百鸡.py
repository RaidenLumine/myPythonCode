# 百钱百鸡问题的白话版：100元钱买100只鸡，公鸡5元1只，母鸡3元1只，小鸡1元3只。问公鸡、母鸡、小鸡各多少只（某种鸡可以为0只）？
# 现在把100改为n，即n元钱买n只鸡，各种鸡价格不变，结果又如何呢？
# 测试数据保证至少存在一组解。

import sys
for line in sys.stdin:
    line=line.strip()
    n=int(line)
    for x in range(n//5+1):
        for y in range(n//3+1):
            z=n-x-y
            if z>=0 and z%3==0 and 5*x+3*y+z//3==n:
                print(f"{x} {y} {z}")
                break