# 当n=5时，沙漏图形如输出样例所示。
# 请观察并明确沙漏图形的规律。要求输入一个整数n，输出满足规律的沙漏图形。

# 输入格式:
# 测试数据有多组，处理到文件尾。每组测试输入一个整数n（1<n<20）。

# 输出格式:
# 对于每组测试，输出满足规律的沙漏图形。

# 输入样例:
# 5
# 输出样例:
# *********
#  *******
#   *****
#    ***
#     *
#    ***
#   *****
#  *******
# *********

import sys
if __name__ == "__main__":
    for line in sys.stdin:
        line=line.strip()
        n = int(line)
        l=2*n-1
        ptr=[""]*l
        for i in range(n):
            idx=n-i-1
            ptr[idx]=" "*idx + "*"*(2*i+1)
            ptr[l-idx-1]=ptr[idx]
        for i in range(l):
            print(ptr[i])