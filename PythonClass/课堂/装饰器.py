import time
class Test1:

    def timer_wrappper(self,func):
        def wrapper():
            start = time.time()
            func()
            end = time.time()
            print(f"{end-start:.2f} s")
        return wrapper

    def work(self):
        print("Working...")
    

    """运行顺序：
        1、调用 work()，实际上调用的是 wrapper()
        2、wrapper() 内部调用 func()，也就是 work()
        3、work() 执行完毕，返回到 wrapper()
        4、wrapper() 计算时间并打印
    """
    
class Test2:
    def timer_decorator(func):
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            print(f"{end-start:.2f} s")
            return result
        return wrapper
    
    @timer_decorator
    def work(self, n):
        print("Working...")
        total = 0
        for i in range(n):
            total += i
        return total
    
    """运行顺序：
        1、调用 work()，实际上调用的是 wrapper()
        2、wrapper() 内部调用 func()，也就是 work()
        3、work() 执行完毕，返回到 wrapper()
        4、wrapper() 计算时间并打印
        5、wrapper() 返回 work() 的结果
    """
    
class Test3:    # 多层装饰器
    def before(func):
        def wrapper(*args, **kwargs):
            print("Before function call")
            return func(*args, **kwargs)
        return wrapper
    
    def after(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            print("After function call")
            return result
        return wrapper
    
    @before
    @after
    def work(self):
        print("Working...")
        
    """运行顺序：
        1、调用 work()，实际上调用的是 before 装饰后的 wrapper()
        2、before 的 wrapper() 内部调用 after 装饰后的 wrapper()
        3、after 的 wrapper() 内部调用实际的 work()
        4、work() 执行完毕，返回到 after 的 wrapper()
        5、after 的 wrapper() 打印 "After function call"，然后返回到 before 的 wrapper()
        6、before 的 wrapper() 打印 "Before function call"
    """
        
    
if __name__ == "__main__":
    t1 = Test1()
    t1.work()
    
    t2 = Test2()
    res = t2.work(1000000)
    print(f"Result from Test2: {res}")
    
    t3 = Test3()
    t3.work()