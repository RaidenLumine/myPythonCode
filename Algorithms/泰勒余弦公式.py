def taylor_cos(x, n):
    t=1.0
    sum=1.0
    for i in range(1,n+1):
        t*=(-x*x)/((2*i-1)*(2*i))
        sum+=t
    return sum

if __name__ == "__main__":
    x, n = input().split()
    x = float(x)
    n = int(float(n))
    print(taylor_cos(x, n))