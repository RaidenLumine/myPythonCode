def index_search(main_table, index_table, target):
    # 二分查找确定块
    low, high = 0, len(index_table) - 1
    while low <= high:
        mid = (low + high) // 2
        block_max, start_pos = index_table[mid]
        if target > block_max:
            low = mid + 1
        elif mid > 0 and target < index_table[mid - 1][0]:
            high = mid - 1
        else:
            # 块内顺序查找
            end_pos = index_table[mid + 1][1] if mid + 1 < len(index_table) else len(main_table)
            for i in range(start_pos, end_pos):
                if main_table[i] == target:
                    return i
            return -1
    return -1

if __name__ == "__main__":
    data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]
    index = [(5, 0), (9, 5)]  # 每个块的（最大值, 起始位置）
    print(index_search(data, index, 6))  # 输出: 7