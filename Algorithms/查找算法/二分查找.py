def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        # 1.二分查找
        mid = (low + high) // 2
        
        # 2.插值查找
        # mid = low + (target - arr[low]) // (arr[high] - arr[low]) * (high - low)
        
        if arr[mid] > target:
            high = mid - 1
        elif arr[mid] < target:
            low = mid + 1
        else:
            return mid
        
    return None

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    target = 6
    result = binary_search(arr, target)
    print("Element found at index:", result)