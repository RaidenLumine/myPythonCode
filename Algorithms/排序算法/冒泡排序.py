from typing import List
import math
class BubbleSort:
    """冒泡排序算法"""
    def bubbleSort(self, arr: List[int]) -> List[int]:
        n = len(arr)
        for i in range(n-1):
            isSwapped = False
            for j in range(n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j],arr[j+1] = arr[j+1],arr[j]   # 交换相邻元素
                    isSwapped = True
            if not isSwapped:   # 如果没有交换，说明数组已经有序，可以提前结束循环，优化算法
                break
        return arr
    
    """有序边界优化"""
    def orderedBoundaryBubbleSort(self, arr: List[int]) -> List[int]:
        n = len(arr)
        boundary = n - 1
        for _ in range(n - 1):
            isSwapped = False
            newBoundary = 0
            for j in range(boundary):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    isSwapped = True
                    newBoundary = j
            boundary = newBoundary
            if not isSwapped:
                break
        return arr

    """双向冒泡排序 (鸡尾酒排序) """
    def deBubbleSort(self, arr: List[int]) -> List[int]:
        n = len(arr)
        left, right = 0, n - 1
        while left < right:
            isSwapped = False
            for j in range(left, right):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    isSwapped = True
            right -= 1
            for j in range(right, left, -1):
                if arr[j] < arr[j - 1]:
                    arr[j], arr[j - 1] = arr[j - 1], arr[j]
                    isSwapped = True
            left += 1
            if not isSwapped:
                break
        return arr
    
    """索引奇偶分类 (奇偶排序) """
    def oddEvenSort(self, arr: List[int]) -> List[int]:
        n = len(arr)
        isSorted = False
        while not isSorted:
            isSorted = True
            for i in range(1, n - 1, 2):
                if arr[i] > arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    isSorted = False
            for i in range(0, n - 1, 2):
                if arr[i] > arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    isSorted = False
        return arr
    
    """个位桶排序"""
    def lsdBucketSort(self, arr: List[int]) -> List[int]:
        if not arr:
            return arr
        
        buckets = [[] for _ in range(10)]
        
        for num  in arr:
            digit = math.fabs(num) % 10
            bucket[digit].append(num)
            
        sortedBuckets = []
        for bucket in buckets:
            if bucket:
                sortedBuckets = BubbleSort().bubbleSort(bucket)
                sortedBuckets.append(bucket)
                
        res = []
        for bucket in sortedBuckets:
            res.extend(bucket)
            
        return res
                
    
if __name__ == "__main__":
    pass