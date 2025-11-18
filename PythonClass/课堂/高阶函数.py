def test1():
    """lambda 函数"""
    """函数名 = lambda 参数: 表达式"""
    
    l = [(lambda x: x ** 2),(lambda x: x ** 3),(lambda x: x ** 4)]
    print(l[0](2), l[1](2), l[2](2))
    
def test2():
    """map 函数"""
    """map(函数, 可迭代对象)"""
    """惰性求值"""
    
    l = [1, 2, 3, 4, 5]
    r = map(lambda x: x ** 2, l)
    print(list(r))  # r 从头开始取值
    print(list(r))  # r 的值已经被取完了
    
def test3():
    """filter 函数"""
    """filter(函数, 可迭代对象)"""
    """惰性求值"""
    
    def larger50(x):
        return x > 50
    
    l = [10, 20, 30, 60, 70, 80]
    r = filter(larger50, l)
    print(list(r))  # r 从头开始取值
    print(list(r))  # r 的值已经被取完了
    
def test4():
    """reduce 函数"""
    """reduce(函数, 可迭代对象)"""
    """惰性求值"""
    
    from functools import reduce
    
    def func(x, y):
        return x + y
    
    l = [1, 2, 3, 4, 5]
    r = reduce(func, l)
    print(r)
    
def test5():
    """reduce 函数实践"""
    
    from functools import reduce
    
    def product(l):
        res = reduce(lambda x, y: x * y, l)
        return res
    
    l = [2,4,6,8]
    r = product(l)
    print(r)
    
def test6():
    """生成器 (generators) """
    """ yield 关键字 """
    
    def get_squares(n):
        return [x*x for x in range(n)]
    
    print(get_squares(5))
    
    def gen_squares(n):
        for x in range(n):
            yield x * x
            
    for val in gen_squares(5):
        print(val)
        
    print(gen_squares(5))
    
    def count_up():
        print("开始")
        
    
    
    
if __name__ == "__main__":
    # test1()
    # test2()
    # test3()
    # test4()
    test5()