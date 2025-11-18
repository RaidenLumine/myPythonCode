from typing import List
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

    def 

if __name__ == "__main__":
    pass