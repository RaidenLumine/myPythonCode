def seleteSort(arr):
    n = len(arr)
    for i in range(n):
        p = i
        for j in range(i+1,n):
            if(arr[p]>arr[j]):
                p=j
        arr[p],arr[i] = arr[i],arr[p]   # 将最小值放到数组前面
    return arr
    
# arr = list(map(float, input().split()))
arr = [5, 2, 9, 1, 5, 6]
print(seleteSort(arr))
    