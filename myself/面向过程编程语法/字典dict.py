# 定义字典
def dict1():
    d1 = {
        "张三": {
            "数学": 95,
            "语文": 90
            }, 
        "李四": {
              "数学": 90,
              "语文": 85
            }, 
        "王五": {
              "数学": 80,
              "语文": 70
            }
        }
    print(d1)
    d2 = dict()
    d3 = {}
    print(f"d2的类型是：{type(d2)}，内容是：{d2}")
    
    d4 = dict(zip(["张三", "李四", "王五"], [95, 90, 80]))
    print(f"d4的类型是：{type(d4)}，内容是：{d4}")
    
    d5 = {name : score for name, score in zip(["张三", "李四", "王五"], [95, 90, 80])}
    print(d5)
    
    d6 = {key : val for key in range(3) for val in range(2)}
    print(d6)
    
    
# 修改、增加元素
def dict2():
    d1 = {"张三": 95, "李四": 90, "王五": 80}
    d1["张三"] = 88
    print(d1)
    d1["赵六"] = 85
    print(d1)
    
# 删除元素
def dict3():
    d1 = {"张三": 95, "李四": 90, "王五": 80}
    del d1["李四"]
    print(d1)
    score = d1.pop("王五")
    print(f"被删除的元素是：{score}, 删除后的字典是：{d1}")
    # del d1["老六"]  # 错误，KeyError: '老六'
    
# 清空字典
def dict4():
    d1 = {"张三": 95, "李四": 90, "王五": 80}
    d1.clear()
    print(f"清空后的字典是：{d1}")
    
# 查找元素
def dict5():
    d1 = {"张三": 95, "李四": 90, "王五": 80}
    score = d1.get("张三", 0)
    print(f"张三的分数是：{score}")
    # score = d1["老六"]  # 错误，KeyError: '老六'
    
# keys() 获取全部键
def dict6():
    d1 = {"张三": 95, "李四": 90, "王五": 80}
    keys = d1.keys()
    print(f"字典的所有键是：{keys}")
    
# for 遍历
def dict7():
    d1 = {"张三": 95, "李四": 90, "王五": 80}
    for key in d1:
        print(f"{key}的分数是：{d1[key]}")
        
# items() 获取键值对
def dict8():
    d1 = {"张三": 95, "李四": 90, "王五": 80}
    items = d1.items()
    print(f"字典的所有键值对是：{items}")
    
# values() 获取所有值
def dict9():
    d1 = {"张三": 95, "李四": 90, "王五": 80}
    values = d1.values()
    print(f"字典的所有值是：{values}")
    
# 字典的嵌套
def dict10():
    d1 = {["张三","老六","金九"]: 95, "李四": 90, "王五": 80}
    print(f"字典的类型是：{type(d1)}，内容是：{d1}")
    print(d1["金九"])
    
# 字典的 while 循环
def dict11():
    d1 = {"张三": 95, "李四": 90, "王五": 80}
    keys = list(d1.keys())
    index = 0
    while index < len(keys):
        key = keys[index]
        print(f"{key}的分数是：{d1[key]}")
        index += 1
        
dict1()
# dict2()
# dict3()
# dict4()
# dict5()
# dict6()
# dict7()
# dict8()
# dict9()
# dict10()
# dict11()
