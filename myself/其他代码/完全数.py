# 输出最小五个完全数

import math

def isPrefectNumber(n: int) -> bool:
    if n < 2:
        return False
    divisorSum = 1
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:  # i是n的一个约数
            divisorSum += i
            if i != n // i: # 避免平方根重复加
                divisorSum += n // i
    return divisorSum == n

def solve(n: int) -> None:
    count = 0
    num = 1
    while count < n:
        if isPrefectNumber(num):
            print(num)
            count += 1
        num += 1

if __name__ == "__main__":
    solve(int(input()))