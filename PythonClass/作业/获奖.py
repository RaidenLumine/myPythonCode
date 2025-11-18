# 在某次竞赛中，判题规则是按解题数从多到少排序，在解题数相同的情况下，按总成绩（保证各不相同）从高到低排序，
# 取排名前60%的参赛队（四舍五入取整）获奖，请确定某个队能否获奖。

# 输入格式:
# 首先输入一个正整数T，表示测试数据的组数，然后是T组测试数据。
# 每组测试的第一行输入1个整数n（1≤n≤15）和1个字符串ms（长度小于10且不含空格），
# 分别表示参赛队伍总数和想确定是否能获奖的某个队名；
# 接下来的n行输入n个队的解题信息，每行一个1个字符串s（长度小于10且不含空格）和2个整数m，g（0≤m≤10，0≤g≤100），
# 分别表示一个队的队名、解题数、成绩。当然，n个队名中肯定包含ms。

# 输出格式:
# 对于每组测试，若某队能获奖，则输出YES，否则输出NO。

# 输入样例:
# 1
# 3 team001
# team001 2 27
# team002 2 28
# team003 0 7
# 输出样例:
# YES

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        n, winner = input().split()
        n = int(n)
        teams = []
        for _ in range(n):
            s, m, g = input().split()
            m = int(m)
            g = int(g)
            teams.append((s, m, g))
        
        teams.sort(key = lambda x: (-x[1], -x[2]))
        
        ddl = len(teams) * 0.6
        if ddl == int(ddl):
            ddl = int(ddl)
        else:
            if ddl - int(ddl) < 0.5:
                ddl = int(ddl)
            else:
                ddl = int(ddl) + 1
                
        isFound = False
        for i in range(ddl):
            if teams[i][0] == winner:
                isFound = True
                print("YES")
                break
        if not isFound:
            print("NO")
        