class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]  # 每个槽位初始化为空列表

    def hash_function(self, key):
        return key % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        for kv in self.table[index]:
            if kv[0] == key:  # 更新已存在的键
                kv[1] = value
                return
        self.table[index].append([key, value])  # 添加新键值对

    def search(self, key):
        index = self.hash_function(key)
        for kv in self.table[index]:
            if kv[0] == key:
                return kv[1]
        return None
    
if __name__ == "__main__":
    hash_table = HashTable()
    hash_table.insert(1, "A")
    hash_table.insert(2, "B")
    hash_table.insert(12, "C")  # 这个会和键1冲突
    print(hash_table.search(1))  # 输出: A
    print(hash_table.search(2))  # 输出: B
    print(hash_table.search(12))  # 输出: C
    print(hash_table.search(3))  # 输出: None