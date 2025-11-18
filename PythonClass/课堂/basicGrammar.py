
"""
    print(value = ..., sep = ' ', end = '\n', file = sys.stdout, flush = False)
    value: 要打印的值，可以是多个，用逗号隔开
    sep: 多个值之间的分隔符，默认是空格
    end: 打印结束后的结尾符，默认是换行符
    file: 打印的目标文件，默认是标准输出(sys.stdout)
    flush: 是否立即刷新输出缓冲区，默认是False
"""

"""
    eval(): 将字符串str当成有效的表达式来求值并返回计算结果
    格式: eval(expression, globals=None, locals=None)
    expression: 要计算的字符串表达式
    globals: 可选参数，指定全局命名空间，必须是字典类型
    locals: 可选参数，指定局部命名空间，可以是任何映射对象
"""

"""
    海象运算符 :=
    作用: 在表达式内部为变量赋值
    格式: 变量 := 表达式
    注意: 变量在赋值前必须已经定义过
    示例:
        if (n := len(some_list)) > 10:
            print(f"List is too long ({n} elements, expected <= 10)")
    等价于：
        n = len(some_list)
        if n > 10:
            print(f"List is too long ({n} elements, expected <= 10)")
"""
