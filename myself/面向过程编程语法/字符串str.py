"""
    字符串看上去不像列表、元组那样，但也是数据容器的一员
    字符串是字符的容器，一个字符串可以放入任意数量的字符
    字符串不可修改，可视为元组
"""

# 字符串初步
def str0():
    str = "I am the bond of my sword"
    print(str[-5])
    
# index 查找
def str1():
    str = "I am the bond of my sword"
    index0 = str.index("am")
    print(index0)
    index1 = str.index(" ")
    print(index1)
    index2 = str.index("x")
    print(index2)
    
# replace(A,B) 替换，将字符串所有的A换成B
# 实质上得到一个新字符串，而不是修改
def str2():
    str = "I am the bond of my sword"
    newStr = str.replace("o","a")
    print(newStr)
    
# split 分割操作，将字符串分割为多个字符串，放入列表中
def str3():
    str = "I am the bond of my sword"
    str_list = str.split(" ")
    print(f"{type(str_list)},{str_list}")
    
# strip 规整操作
# 1. 字符串.strip() 不传参数时使用默认数字，去除前后空格，并返回结果
def str4():
    str = "  I am the bond of my sword   "
    newStr = str.strip()
    print(newStr)
    
# 2. 传参数时，从首和尾遍历操作字符串，若存在字符是参数中包含的则删去第一个出现的字符，直到不包含为止
def str5():
    str = "I am the bond of my swordI"
    newStr = str.strip("I")
    print(newStr)
    
# count 统计给定字符的个数
def str6():
    str = "I am the bond of my sword"
    num = str.count("o")
    print(num)
    
# len 统计字符串长度
def str7():
    str = "I am the bond of my sword"
    num = len(str)
    print(num)
    


# str0()
str1()
#str2()
#str3()
# str4()
# str5()
#str6()
#str7()
