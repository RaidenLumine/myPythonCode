"""
    'enumerate' 函数的使用方法
    enumerate(iterable, start=0)
    参数说明：
    iterable: 一个可迭代对象，如列表、元组或字符串
    start: 可选参数，指定索引的起始值，默认为0
    返回值：返回一个枚举对象，该对象生成包含索引和值的元组
    示例代码：
    fruits = ['apple', 'banana', 'cherry']
    for index, fruit in enumerate(fruits):
        print(f"Index: {index}, Fruit: {fruit}")
    fruits = ['apple', 'banana', 'cherry']
    for index, fruit in enumerate(fruits, start=1):
        print(f"Index: {index}, Fruit: {fruit}")
"""

def test1():
    fruits = ['apple', 'banana', 'cherry']
    for index, fruit in enumerate(fruits):
        print(f"Index: {index}, Fruit: {fruit}")
        
if __name__ == "__main__":
    test1()