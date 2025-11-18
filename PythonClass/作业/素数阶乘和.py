# 求其中素数的阶乘和
# 分数 20
# 作者 刘益玲
# 单位 集美大学
#  输入N（N不大于10）个数，求其中素数的阶乘和。
#  先输入一个不大于10的数（表示输入数据的总个数），然后再从键盘输入N个数，判断这些数否是素数，并对其中所有素数求阶后累加。

# 如果N>10，则输出"Too big!Game over!"，程序终止运行；
# 如果输入的是非数字，则输出"Input Error!",程序终止运行；
# 正常输入、输出情况如下：
# 例如以下输入后是计算 3！+7！=5046
# 输入格式:
# 3
# 3
# 6
# 7
# 输出格式:
# 5046
# 输入样例:
# 在这里给出一组输入。例如：
# 3
# 3
# 6
# 7
# 输出样例:
# 在这里给出相应的输出。例如：
# 5046

import math
from typing import List

def isTooBig(N: int) -> bool:
    return N > 10

def isDigit(s: str) -> bool:
    return s.isdigit()

def isPrime(num: int) -> bool:
    if num < 2:
        return False
    for i in range(2, math.floor(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def main():
    N = input()
    if not isDigit(N):
        print("Input Error!")
        return
    N = int(N)
    if isTooBig(N):
        print("Too big!Game over!")
        return
    
    nums: List[int] = []
    for _ in range(N):
        num = input()
        if not isDigit(num):
            print("Input Error!")
            return
        num = int(num)
        if isTooBig(num):
            print("Too big!Game over!")
            return
        elif isPrime(num):
            nums.append(num)
            
    summary = sum(math.factorial(num) for num in nums)
    print(summary)
        
if __name__ == '__main__':
    main()