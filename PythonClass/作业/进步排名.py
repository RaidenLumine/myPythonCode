# 假设每个学生信息包括用户名、进步总数和解题总数。解题进步排行榜中，按进步总数及解题总数生成排行榜。
# 要求先输入n个学生的信息；然后按进步总数降序排列；
# 若进步总数相同，则按解题总数降序排列；
# 若进步总数和解题总数都相同，则排名相同，但输出信息时按用户名升序排列，否则排名为排序后相应的序号。

# 输入格式:
# 首先输入一个整数T，表示测试数据的组数，然后是T组测试数据。
# 每组测试数据先输入一个正整数n（1 < n < 50），表示学生总数。
# 然后输入n行，每行包括一个不含空格的字符串s（不超过8位）和2个正整数d和t，分别表示用户名、进步总数和解题总数。

# 输出格式:
# 对于每组测试，输出最终排名。每行一个学生的信息，分别是排名、用户名、进步总数和解题总数。
# 每行的各个数据之间留一个空格。

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        n = int(input())
        students = []
        for _ in range(n):
            s,d,t=input().split()
            students.append((s,int(d),int(t)))
        students.sort(key=lambda x:(-x[1],-x[2],x[0]))
        rank = 1
        for i in range(n):
            # 注意排名相同的情况
            if i > 0 and students[i][1] == students[i-1][1] and students[i][2] == students[i-1][2]:
                print(rank, students[i][0], students[i][1], students[i][2])
            else:
                rank = i + 1
                print(rank, students[i][0], students[i][1], students[i][2])