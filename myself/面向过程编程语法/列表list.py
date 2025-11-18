"""
    列表 list 的定义与使用
    列表的索引
    列表的操作
        1.查询元素
        2.修改元素
        3.插入元素
        4.追加元素
        5.删除元素
        6.统计某个元素在列表的数量
        7.统计列表中元素的数量
        8.列表的 while 循环
        9.列表的 for 循环
    
"""

# 列表初步
def list0():
    name = ['heima',666,True,[10,'cs'],(1015,str(97))] # 类型不受限制，可考虑列表嵌套
    print(f"{name},{type(name)}")
    l1 = [1,]
    print(f"{l1},{type(l1)}")

# 列表索引
def list1():
    name = ['Lily','Tom','Rose']
    print(name[0]) # 正向索引 第1个
    print(name[-1]) # 反向索引 最后一个
    # print(name[3]) # 错误，超出列表范围

# 列表操作
# 1.查询元素（index.(元素)，从前往后，查不到就报错 ValueError）
def list2():
    myList1 = ['itcast','itheima','itheima','itheima','python']
    index = myList1.index('itheima')
    print(f"itheima在列表中的下标hello索引是：{index}")
    # index = myList1.index('hello')
    # print(f"itheima在列表中的下标索引是：{index}")

# 2.修改元素
def list3():
    myList1 = ['itcast','itheima','python']
    myList1[0] = '晚安华师'
    print(f"修改元素后的列表为：{myList1}")

# 3.插入元素（）insert(下标，元素)
def list4():
    myList1 = ['itcast','itheima','python']
    myList1.insert(1,'best')
    print(f"插入元素后的列表为：{myList1}")

# 4.追加元素
# # 1）用append加到列表最后，append(元素)
def list5():
    myList1 = ['itcast','itheima','python']
    print(f"追加前列表为：{myList1}, 地址为: {id(myList1)}")
    myList1.append('emiya')
    print(f"追加单个元素后的列表为：{myList1}, 地址为: {id(myList1)}")

# 2）用extend将多个元素加到给定列表最后
def list6():
    myList1 = ['itcast','itheima','python']
    print(f"追加前列表为：{myList1}, 地址为: {id(myList1)}")
    myList1.extend(['I','am','the','bond','of','my','sword'])
    print(f"追加多个元素后的列表为：{myList1}, 地址为: {id(myList1)}")
    # myList1.extend('steel')
    # print(f"追加字符串后的列表为：{myList1}")

# 5.删除元素
# 1）del 列表[下标]
def list7():
    myList2 = ['itcast','itheima','python']
    del myList2[2]
    print(f"删除第3个元素后的列表为：{myList2}")

# 2）列表.pop(下标)，取出对应元素, 默认删除最后一个元素
def list8():
    myList2 = ['itcast','itheima','python']
    deleted = myList2.pop(1)
    print(f"删除第2个元素后的列表为：{myList2}，被删除的元素为：{deleted}")

# 3）列表.remove(元素)：从前到后找到第一个与该值相同的元素
def list9():
    myList2 = ['itcast','itheima','python']
    myList2.remove('python')
    print(f"移除元素后的列表为：{myList2}")

# 4）列表.clear()：清空列表
def list10():
    myList2 = ['itcast','itheima','python']
    myList2.clear()
    print(f"清空后的列表为：{myList2}")

# 6.统计某个元素在列表的数量（列表.count(元素)）
def list11():
    myList3 = ['itcast','itcast','itcast','python']
    count = myList3.count('itcast')
    print(f"列表中 itcast 的数量为：{count}")

# 7.统计列表中元素的数量（len(列表)）
def list12():
    myList3 = ['itcast','itcast','itcast','python']
    count = len(myList3)
    print(f"列表中元素的数量为：{count}")
    
# 8.列表的 while 循环
def list13():
    mylist1 = ['I','am','the','bond','of','my','sword']
    index = 0
    while index < len(mylist1):
        print(mylist1[index])
        index += 1
        
# 9.列表的 for 遍历
def list14():
    mylist2 = ['Steel','is','my','body','and','fire','is','my','blood']
    for i in mylist2:
        print(i)

# 10. 列表的排序 ( 此时列表被永久改变 )
# 1) sort()：默认升序排序
def list15():
    myList1 = [3,1,4,5,2]
    print(f"排序前列表为：{myList1}")
    myList1.sort()
    print(f"排序后列表为：{myList1}")
    myList1.sort(reverse=True)
    print(f"降序排序后列表为：{myList1}")
    
# 2) sorted(列表)：返回一个新的排序后的列表，原列表不变
def list16():
    myList1 = [3,1,4,5,2]
    print(f"排序前列表为：{myList1}")
    sortedList = sorted(myList1)
    print(f"排序后新列表为：{sortedList}")
    print(f"原列表仍为：{myList1}")
    sortedList2 = sorted(myList1, reverse=True)
    print(f"降序排序后新列表为：{sortedList2}")
    
# 11. 列表的迭代器
def list17():
    myList1 = ['itcast','itheima','python']
    it = iter(myList1)
    # print(next(it))
    # print(next(it))
    # print(next(it))
    # print(next(it)) # 超出范围会报错 StopIteration
    # while True:
    #     try:
    #         print(next(it))
    #     except StopIteration:
    #         break
    for item in it:
        print(item)
        
# 12. 列表推导式
def list18():
    import math
    # 生成1-10的平方列表
    squares = [int(math.pow(x, 2)) for x in range(1,11)]
    print(f"1-10的平方列表为：{squares}")
    
    # 生成1-10中偶数的平方列表
    even_squares = [int(math.pow(x, 2)) for x in range(1,11) if x % 2 == 0]
    print(f"1-10中偶数的平方列表为：{even_squares}")
    
# 13. 列表推导式-平铺
def list19():
    vec = [
        [1,2,3], 
        [4,5,6], 
        [7,8,9]
    ]
    flat_list = [num for sublist in vec for num in sublist]
    print(f"平铺后的列表为：{flat_list}")

def main():
    pass
    # list0()
    # list1()
    list2()
    # list3()
    # list4()
    # list5()
    # list6()
    # list7()
    # list8()
    # list9()
    # list10()
    # list11()
    # list12()
    # list13()
    # list14()
    # list15()
    # list16()
    # list17()
    # list18()
    # list19()
    
if __name__ == "__main__":
    main()