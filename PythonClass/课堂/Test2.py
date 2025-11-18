def test1():
    x=3.0
    y=3.0
    print(id(x)==id(y))

def test2():
    x=30000
    y=3.14
    print(id(x)==id(y))
    
def test3():
    x, y = 30000, 3.14
    print(id(x) == id(y))
    
if __name__ == "__main__":
    test1()
    test2()
    test3()