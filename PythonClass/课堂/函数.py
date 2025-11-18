class Temperature:
    def celiusToFahrenheit(self, c: float) -> float:
        return (c * 9/5) + 32

    def fahrenheitToCelius(self, f: float) -> float:
        return (f - 32) * 5/9

def test1() -> None:
    temp = Temperature()
    
    c = 25
    f = temp.celiusToFahrenheit(c)
    print(f"{c}°C is {f}°F")
    
    f = 77
    c = temp.fahrenheitToCelius(f)
    print(f"{f}°F is {c}°C")
    
def test2() -> None:
    print("外层函数")
    
    def inner():
        print("内层函数")
        
    inner()
    
def test3():
    def demo(newItem, oldList = []):
        oldList.append(newItem)
        return oldList
    
    print(demo('5',[1,2,3,4]))
    print(demo('aaa',['a','b']))
    print(demo('a'))    # 输出 ['a']
    print(demo('b'))    # 输出 ['a', 'b'], 因为默认参数只在函数定义时被计算一次
    print(demo('c'))    # 输出 ['a', 'b', 'c']
    
def test4():    # 全局变量和局部变量 1
    def demo():
        global x
        x = 3
        y = 4
        print(x,y)
        
    x = 5
    demo()
    
    del x
    try:
        print(x)
    except NameError as e:
        print("x 已被删除，无法访问。")
    
    try:
        print(y)
    except NameError as e:
        print("y 在函数外部无法访问。")
        
    demo()
    
def test5():    # 局部变量和全局变量 2
    x = 3
    def outer():
        y=5
        def eval():
            return '我是假的 eval() 函数'
        def inner():
            x=7
            y=9
            print('inner:',x,y,max(x,y),eval())
            
        inner()
        print('outer:',x,y,max(x,y),eval())
        
    outer()
    print(eval("1+1"))
    
from typing import Callable
def test6() -> Callable:    # 函数闭包 1
    count = 0
    def counter():
        nonlocal count
        count+=1
        return count
    
    return counter

def test7():                # 函数闭包 2
    def makePower(y):
        def func(x):
            return x**y
        return func
    
    square = makePower(2)
    cube = makePower(3)
    print(square(5))  # 输出 25
    print(cube(5))    # 输出 125
    
def test8():
    # 变量访问顺序： 局部变量 -> 外层函数变量 -> 全局变量 -> 内置变量
    
    def scope_test():
        def do_local():
            spam = "local"

        def do_nonlocal():
            nonlocal spam
            spam = "no local, no global"

        def do_global():
            global spam
            spam = "global"

        spam = "original"
        do_local()
        print(spam)     # 输出 "test"
        
        do_nonlocal()
        print(spam)     # 输出 "no local, no global"
        
        do_global()
        print(spam)     # 输出 "no local, no global"
        
    scope_test()
    print(spam)     # 输出 "global"
    
if __name__ == "__main__":
    # test1()
    # test2()
    # test3()
    # test4()
    # test5()
    
    # timer1 = test6()
    # timer2 = test6()
    # print(timer1()) # 输出 1
    # print(timer1()) # 输出 2
    # print(timer2()) # 输出 1
    
    # test7()
    test8()