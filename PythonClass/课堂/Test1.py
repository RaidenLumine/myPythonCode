def test1():
    a=0.4
    b=0.3
    print(a-b)
    
def test2():
    import math
    a=0.4
    b=0.3
    print(math.isclose(a-b,0.1))
    
# 短路求值
def test3():
    a=3.14
    b=2
    print(a and b)
    
# 进制转换
def test4():
    a=12
    print(bin(a))   # 二进制
    print(oct(a))   # 八进制
    # print(int(a,2))   # 十进制
    print(hex(a))   # 十六进制
    
# 内置数值计算函数
def test5():
    a=3
    b=2
    print(abs(-a))     # 绝对值
    print(pow(a,b))    # 幂运算
    print(pow(a,b,2))  # 幂运算，对2取模
    print(round(a,b))  # 四舍五入，保留b位小数, 遵循银行家舍入法
    print(divmod(a,b)) # 商和余数
    
    
if __name__ == "__main__":
    # test1()
    # test2()
    # test3()
    # test4()
    test5()
