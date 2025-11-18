def rotate(arr,n):
    if not arr:
        return arr
    if n < 0:
        raise ValueError("n 不能是负数！")
    
    n = n % len(arr)
    return arr[:-n]+arr[-n:]

if __name__ == "__main__":
    s = input("请输入一个字符串：")
    try:
        n = int(input("请输入旋转的位数："))
        print("旋转后的字符串是：", rotate(s,n))
    except ValueError as e:
        print("输入错误：", e)