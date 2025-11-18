"""
    'zip' 函数的使用方法：
    zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。
    如果传入的参数长度不等，则返回列表长度与最短的对象相同。
    语法：
    zip(*iterables)
    参数说明：
    iterables -- 一个或多个可迭代的对象，如列表、元组、字符串等。
    返回值：
    返回一个由元组组成的列表，每个元组包含来自各个可迭代对象中对应位置的元素。
    示例：
    >>> list1 = [1, 2, 3]
    >>> list2 = ['a', 'b', 'c']
    >>> zipped = zip(list1, list2)
    >>> print(list(zipped))
    [(1, 'a'), (2, 'b'), (3, 'c')]
    >>> list3 = [True, False]
    >>> zipped = zip(list1, list2, list3)
    >>> print(list(zipped))
    [(1, 'a', True), (2, 'b', False)]
"""

def test1():
    list1 = [1, 2, 3]
    list2 = ['a', 'b', 'c']
    zipped = zip(list1, list2)
    print(list(zipped))
    
def test2():
    list1 = [1, 2, 3]
    list2 = ['a', 'b', 'c']
    list3 = [True, False]
    zipped = zip(list1, list2, list3)
    print(list(zipped))
    
if __name__ == "__main__":
    # test1()
    test2()