def test1() -> None:
    for c in ['a', 'b', 'c']:
        print(c, end=' ')
    print()

def test2() -> None:
    for i in range(1,10):
        for j in range(1,i+1):
            print(f"{j} x {i} = {i * j}", end = ' ')
        print()
        
def test3() -> None:
    data = [1,3,5,8]
    count = 0
    for i in data:
        for j in data:
            for k in data:
                if i != j and j != k and i != k:
                    count += 1
                    print(f"{100 * i + 10 * j + k}", end = '\t')
                    if count % 10 == 0:
                        print()
    print(f"\ncount = {count}")
    
def test4() -> None:
    from ast import literal_eval
    
    while (content:=literal_eval(input("请输入一个列表："))) != 0:
        match content:
            case [1,2,3,4,*_]:
                print("前4项匹配成功")
            case [1,2,3,*_]:
                print("前3项匹配成功")
            case [1,2,*_]:
                print("前2项匹配成功")
            case [1,*_]:
                print("前1项匹配成功")
            case [*_]:
                print("匹配失败")
            case _:
                print("格式错误")
                
def test5() -> None:
    import math
    
    def isPrime(n:int) -> bool:
        if n <= 1:
            return False
        for i in range(2, int(math.sqrt(n))+1):
            if n % i == 0:
                return False
        return True
    
    while (num:=int(input("请输入一个整数："))) != 0:
        if isPrime(num):
            print(f"{num}是素数")
        else:
            print(f"{num}不是素数")
    
    print("程序结束")
            
def test6() -> None:
    count = 0
    for i in range(100,201):
        if i % 3 != 0:
            print(i, end = ' ')
            count += 1
            if count % 10 == 0:
                print()
            continue
        
def test7() -> None:
    from ast import literal_eval
    
    while(s:=literal_eval(input("请输入一个整数："))) != 0:
        match s:
            case int() if s < 0:
                print("负数")
            case int() if s == 0:
                print("零")
            case int() if s > 0:
                print("正数")
            case _:
                print("不是整数")


if __name__ == '__main__':
    # test1()
    test2()
    # test3()
    # test4()
    # test5()
    # test6()
    # test7()

    pass
    