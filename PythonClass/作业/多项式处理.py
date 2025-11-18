# 编写程序实现两个多项式相加。例如：

#    p(x)=5x 
# 10
#  +8x 
# 5
#  -x+10
#      g(x)=3x 
# 8
#  +x-3
#      f(x)+g(x)=5x 
# 10
#  +8x 
# 5
#  +3x 
# 8
#  +7

# 输入格式:
# 在第一行输入第一个多项式。如p(x)=5x 
# 10
#  +8x 
# 5
#  -x+10输入是：  5 10, 8 5, -1 1, 10 0
# 在第二行输入第二个多项式。如g(x)=3x 
# 8
#  +x-3输入是：3 8, 1 1, -3 0
# 在第三行输入x指数值,如x指数值是1，x 
# 2
#  指数值是2。

# 输出格式:
# 对应输入的x指数值，输出多项式和中这项的系数。

def parse(poly: str) -> dict:
    parsed = dict()
    if not poly:
        return parsed
    terms = poly.split(',')
    for term in terms:
        term = term.strip()
        if term:
            coef,exp=map(int,term.split())
            parsed[exp] = parsed.get(exp,0)+coef
    return parsed

def add(poly1: dict, poly2: dict) -> dict:
    res = poly1.copy()
    
    for exp,coef in poly2.items():
        res[exp] = res.get(exp,0)+coef
        
    return {exp:coef for exp, coef in res.items() if coef != 0}

if __name__ == '__main__':
    func1 = input().strip()
    func2 = input().strip()
    x = int(input().strip())
    
    poly1 = parse(func1)
    poly2 = parse(func2)
    
    res = add(poly1,poly2)
    
    print(res.get(x,0))