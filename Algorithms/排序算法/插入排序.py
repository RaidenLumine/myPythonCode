# 插入排序
def insertion_sort(arr):
    # 遍历数组中的所有元素
    for i in range(1, len(arr)):
        # 当前要插入的元素
        key = arr[i]
        # 前一个元素的索引
        j = i - 1
        # 移动元素大于key的元素
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        # 插入key到正确的位置
        arr[j + 1] = key
        
def insertion_sort_desc(arr):
    """原地插入排序（降序）。"""
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# 二分插入排序
def binary_insertion_sort(arr):
    # 遍历数组中的所有元素
    for i in range(1, len(arr)):
        key = arr[i]
        left, right = 0, i - 1
        # 使用二分查找找到插入位置
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] > key:
                right = mid - 1
            else:
                left = mid + 1
        # 将元素移到正确位置
        for j in range(i, left, -1):
            arr[j] = arr[j - 1]
        arr[left] = key
        
if __name__ == "__main__":
    arr = [5, 2, 9, 1, 5, 6]
    insertion_sort(arr)
    # binary_insertion_sort(arr)
    print("Sorted array:", arr)