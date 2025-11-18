# 给你一个数组 nums ，请你完成两类查询。
# 其中一类查询要求 更新 数组 nums 下标对应的值
# 另一类查询要求返回数组 nums 中索引 left 和索引 right 之间（ 包含 ）的nums元素的 和 ，其中 left <= right

# 实现 NumArray 类：
# NumArray(int[] nums) 用整数数组 nums 初始化对象
# void update(int index, int val) 将 nums[index] 的值 更新 为 val
# int sumRange(int left, int right) 返回数组 nums 中索引 left 和索引 right 之间
# （ 包含 ）的nums元素的 和 （即，nums[left] + nums[left + 1], ..., nums[right]）

# 示例 1：
# 输入：
# ["NumArray", "sumRange", "update", "sumRange"]
# [[[1, 3, 5]], [0, 2], [1, 2], [0, 2]]
# 输出：
# [null, 9, null, 8]
# 解释：
# NumArray numArray = new NumArray([1, 3, 5]);
# numArray.sumRange(0, 2); // 返回 1 + 3 + 5 = 9
# numArray.update(1, 2);   // nums = [1,2,5]
# numArray.sumRange(0, 2); // 返回 1 + 2 + 5 = 8

# 提示：
# 1 <= nums.length <= 3 * 104
# -100 <= nums[i] <= 100
# 0 <= index < nums.length
# -100 <= val <= 100
# 0 <= left <= right < nums.length
# 调用 update 和 sumRange 方法次数不大于 3 * 104 


# Your NumArray object will be instantiated and called as such:
# NumArray* obj = new NumArray(nums);
# obj->update(index,val);
# int param_2 = obj->sumRange(left,right);

from typing import List

class NumArray:
    
    tree=[]

    def __init__(self, nums: List[int]):
        n=len(nums)
        self.nums=nums
        self.tree=[0]*(n+1)
        for i in range(n):
            self.add(i+1,nums[i])

    def update(self, index: int, val: int) -> None:
        self.add(index+1,val-self.nums[index])
        self.nums[index]=val

    def sumRange(self, left: int, right: int) -> int:
        return self.query(right+1)-self.query(left)

    def lowbit(self,x:int)->int:
        return x&-x

    def add(self,x:int,u:int)->None:
        while x<len(self.nums):
            self.tree[x]+=u
            x+=self.lowbit(x)

    def query(self,x:int)->int:
        ans=0
        i=x
        while i>0:
            ans+=self.tree[i]
            i-=self.lowbit(i)
        return ans

if __name__ == "__main__":
    nums = [1, 3, 5]
    numArray = NumArray(nums)
    print(numArray.sumRange(0, 2))  # 返回 9
    numArray.update(1, 2)            # nums = [1,2,5]
    print(numArray.sumRange(0, 2))  # 返回 8