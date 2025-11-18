"""
    元组 tuple 的定义与使用
    元组的定义：使用小括号 () 定义，元素之间用逗号分隔
    元组的特点：有序、不可变、允许重复
    元组的访问方法: 与列表类似，通过下标索引访问
    单元素元组的定义：需要在元素后添加逗号
    元组的嵌套：元组内可以包含元组
    元组的下标索引: 从0开始, 支持正向和反向索引
    元组的常用操作: index、count、len
    元组的遍历: while 循环、for 循环
    元组的修改：元组本身不可变，但元组内的可变元素（如列表）可以修改
"""



# 定义元组
def tuple1():
    t1 = (1,"Hello",True)
    t2 = ()
    t3 = tuple()
    t4 = "I","am","the","bone","of","my","sword"
    print(f"t1的类型是：{type(t1)}，内容是：{t1}")
    print(f"t2的类型是：{type(t2)}，内容是：{t2}")
    print(f"t3的类型是：{type(t3)}，内容是：{t3}")
    print(f"t4的类型是：{type(t4)}，内容是：{t4}")

# 定义单元素元组
def tuple2():
    t1 = (1)
    print(f"t1的类型为：{type(t1)}，内容是：{t1}")
    t2 = (1,)
    print(f"t2的类型为：{type(t2)}，内容是：{t2}")
    
# 元组的嵌套
def tuple3():
    t1 = ((1,2,3),(4,5,6))
    print(f"t1的类型为：{type(t1)}，内容是：{t1}")
    
# 下标索引取内容
def tuple4():
    t1 = ((1,2,3),(4,5,6))
    num = t1[1][2]
    print(num)
    
# index 查找元组数据
def tuple5():
    t1 = (1,"Hello",True)
    index = t1.index("Hello")
    print(index)
    
# count 统计元组某个元素的数量
def tuple6():
    t1 = (1,"Hello","Hello","Hello","Hello",True)
    count = t1.count("Hello")
    print(count)
    
# len 获取元组的元素数量
def tuple7():
    t1 = (1,"Hello","Hello","Hello","Hello",True)
    print(len(t1))
    
# 元组的 while 循环
def tuple8():
    t1 = (1,"Hello","Hello","Hello","Hello",True)
    index = 0
    while index < len(t1):
        print(t1[index])
        index += 1
    
# 元组的 for 遍历
def tuple9():
    t1 = (1,"Hello",True,True,"Hello",True)
    for i in t1:
        print(i)
        
# 元组本身不能修改
def tuple10():
    t1 = (1,"Hello",True,True,"Hello",True)
    # t1[0] = 2
    
# 元组内的可变元素可以修改，包括列表和字典
def tuple11():
    t2 = (1,"Hello",[123,456,True,"爱你"],{"name":"itheima","age":18})
    t2[2][2] = False
    print(t2[2][2])
    
# 删除元组
def tuple12():
    t1 = (1,"Hello",True)
    del t1
        
if __name__ == '__main__':
    pass
    tuple1()
    # tuple2()
    # tuple3()
    # tuple4()
    # tuple5()
    # tuple6()
    # tuple7()
    # tuple8()
    # tuple9()
    # tuple10()
    # tuple11()