# 7-4 统计各行业就业的学生数量，按数量从高到低方式输出。
# 分数 25
# 作者 魏峻
# 单位 陕西理工大学
# 键盘输入某班各个同学就业的行业名称，行业名称之间用空格间隔(回车结束输入) 。统计各行业就业的学生数量，按数量从高到低方式输出。

# 输入格式:
# 输入各个同学行业名称，行业名称之间用空格间隔（回车结束输入）

# 交通 金融 计算机 交通 计算机 计算机 

# 输出格式:
# 输出参考格式如下，其中冒号为英文冒号：

# 计算机：3

# 交通：2 

# 金融：1

# 输入样例:
# 交通 金融 计算机 交通 计算机 计算机
# 输出样例:
# 计算机:3
# 交通:2
# 金融:1

if __name__ == "__main__":
    count = dict()
    lines = input().split()
    
    for line in lines:
        if line in count:
            count[line] += 1
        else:
            count[line] = 1
    
    sortedDict = dict(sorted(count.items(), key = lambda i: i[1], reverse = True))
    
    for k, v in sortedDict.items():
        print(f"{k}:{v}")