import time
import random

########################################

def test1():
    begin = 1
    end = 500000
    num = 5000
    rep = 10

    start_time = time.time()

    for _ in range(rep):
        data = []
        while len(data) < num:
            ele = random.randint(begin, end)
            if ele not in data:
                data.append(ele)
                
    end_time = time.time()

    # print(f"生成不重复列表： {data}")
    print(f"执行时间：{end_time - start_time:.6f} 秒")

def test2():
    begin = 1
    end = 500000
    num = 5000
    rep = 10

    start_time = time.time()

    for _ in range(rep):
        data = set()
        while len(data) < num:
            ele = random.randint(begin, end)
            if ele not in (data):
                data.add(ele)
                
    end_time = time.time()

    # print(f"生成不重复集合： {data}")
    print(f"执行时间：{end_time - start_time:.6f} 秒")

def test3():
    pass
    countries = {
        "中国": "北京",
        "美国": "华盛顿",
        "英国": "伦敦",
        "法国": "巴黎",
        "德国": "柏林"
    }
    
    countries.setdefault("日本", "东京")
    
    for key in countries:
        print(key)
        
    for key in countries.keys():
        print(key)
        
    for item in countries.items():
        print(item)
        
    for key, val in countries.items():
        print(key,val)

if __name__ == "__main__":
    # test1()
    # test2()
    test3()
    