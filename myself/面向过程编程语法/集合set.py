# 定义集合
def set1():
    s = {1, 2, 3, 4, 5}
    # s1 = {} # 这不是集合，而是空字典
    s2 = set()
    s3 = {1}
    print(f"集合的类型是：{type(s)}，内容是：{s}")
    
    fs = frozenset()
    
# add 添加元素
def set2():
    s = {1, 2, 3}
    s.add(4)
    print(f"集合的类型是：{type(s)}，内容是：{s}")

# remove 删除元素
def set3():
    s = {1, 2, 3, 4, 5}
    s.remove(3)
    print(f"集合的类型是：{type(s)}，内容是：{s}")
    
# pop 随机删除一个元素
def set4():
    s = {1, 2, 3, 4, 5}
    removed_element = s.pop()
    print(f"集合的类型是：{type(s)}，内容是：{s}，被删除的元素是：{removed_element}")
    
# discard 删除元素（如果元素不存在，不会报错）
def set4_discard():
    s = {1, 2, 3, 4, 5}
    s.discard(6)  # 元素6不存在，但不会报错
    print(f"集合的类型是：{type(s)}，内容是：{s}，尝试删除不存在的元素6")
    
# clear 清空集合
def set5():
    s = {1, 2, 3, 4, 5}
    s.clear()
    print(f"集合的类型是：{type(s)}，内容是：{s}，集合已被清空")
    
# difference 求差集
def set6():
    s1 = {1, 2, 3, 4, 5}
    s2 = {4, 5, 6, 7, 8}
    diff = s1.difference(s2)
    print(f"集合s1的差集是：{diff}")
    
# difference_update 求差集并更新
def set7():
    s1 = {1, 2, 3, 4, 5}
    s2 = {4, 5, 6, 7, 8}
    s1.difference_update(s2)
    print(f"集合s1更新后的内容是：{s1}")
    
# intersection 求交集
def set8():
    s1 = {1, 2, 3, 4, 5}
    s2 = {4, 5, 6, 7, 8}
    inter = s1.intersection(s2)
    print(f"集合s1和s2的交集是：{inter}")
    
# intersection_update 求交集并更新
def set9():
    s1 = {1, 2, 3, 4, 5}
    s2 = {4, 5, 6, 7, 8}
    s1.intersection_update(s2)
    print(f"集合s1更新后的内容是：{s1}")
    
# union 求并集
def set10():
    s1 = {1, 2, 3, 4, 5}
    s2 = {4, 5, 6, 7, 8}
    union_set = s1.union(s2)
    print(f"集合s1和s2的并集是：{union_set}")
    
# update 并集并更新
def set11():
    s1 = {1, 2, 3, 4, 5}
    s2 = {4, 5, 6, 7, 8}
    s1.update(s2)
    print(f"集合s1更新后的内容是：{s1}")
    
# isdisjoint 判断两个集合是否不相交
def set12():
    s1 = {1, 2, 3}
    s2 = {4, 5, 6}
    is_disjoint = s1.isdisdisjoint(s2)
    print(f"集合s1和s2是否不相交：{is_disjoint}")
    
# issubset 判断一个集合是否是另一个集合的子集
def set13():
    s1 = {1, 2}
    s2 = {1, 2, 3, 4, 5}
    is_subset = s1.issubset(s2)
    print(f"集合s1是否是集合s2的子集：{is_subset}")
    
# issuperset 判断一个集合是否是另一个集合的超集
def set14():
    s1 = {1, 2, 3, 4, 5}
    s2 = {1, 2}
    is_superset = s1.issuperset(s2)
    print(f"集合s1是否是集合s2的超集：{is_superset}")
    
# 集合推导式
def set15():
    s = {x**2 for x in range(10) if x % 2 == 0}
    print(f"通过集合推导式生成的集合是：{s}")
    
if __name__ == "__main__":
    # set1()
    # set2()
    # set3()
    # set4()
    # set4_discard()
    # set5()
    # set6()
    # set7()
    # set8()
    # set9()
    # set10()
    # set11()
    # set12()
    # set13()
    # set14()
    set15()
