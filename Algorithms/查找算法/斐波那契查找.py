def fibonacci_search(arr, target):
    """
    使用斐波那契查找算法在有序数组中查找目标值。

    Args:
        arr (list): 有序的整数列表。
        target (int): 要查找的目标值。

    Returns:
        int: 如果找到目标值，则返回其索引；否则返回 -1。
    """
    n = len(arr)
    if n == 0:
        return -1

    # 初始化斐波那契数
    fib_m2 = 0  # (m-2)'th Fibonacci No.
    fib_m1 = 1  # (m-1)'th Fibonacci No.
    fib_m = fib_m2 + fib_m1  # m'th Fibonacci

    # 找到最小的斐波那契数 fib_m，使得 fib_m >= n
    while fib_m < n:
        fib_m2 = fib_m1
        fib_m1 = fib_m
        fib_m = fib_m2 + fib_m1

    offset = -1

    # 当数组还有元素需要检查时循环
    # 注意：我们将数组想象成长度为 fib_m
    while fib_m > 1:
        # 检查 arr[i]
        i = min(offset + fib_m2, n - 1)

        # 如果 target 大于 arr[i] 的值，则向右切割数组
        if arr[i] < target:
            fib_m = fib_m1
            fib_m1 = fib_m2
            fib_m2 = fib_m - fib_m1
            offset = i
        # 如果 target 小于 arr[i] 的值，则向左切割数组
        elif arr[i] > target:
            fib_m = fib_m2
            fib_m1 = fib_m1 - fib_m2
            fib_m2 = fib_m - fib_m1
        # 找到元素
        else:
            return i

    # 检查最后一个元素
    if fib_m1 and n > offset + 1 and arr[offset + 1] == target:
        return offset + 1

    # 元素未找到
    return -1

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    target = 6
    result = fibonacci_search(arr, target)
    print("Element found at index:", result)