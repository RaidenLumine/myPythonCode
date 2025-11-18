from math import *

def test1():
    print(0.1+0.2+0.3)
    print(fsum([0.1,0.2,0.3]))   # 精确求和

def isLeapYear(year: int) -> bool:
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)

def getE() -> float:
    i, e, t = 1, 1, 1
    while 1/t > 1e-6:
        t *= i
        e += 1/t
        i += 1
    return e

if __name__ == "__main__":
    test1()
    print(isLeapYear(2000))
    print(getE())
