# 给你一个长度为 n 的整数数组 nums 和 一个目标值 target。
# 请你从 nums 中选出三个整数，使它们的和与 target 最接近。返回这三个数的和。
# 假定每组输入只存在恰好一个解。

# 示例 1：
# 输入：nums = [-1,2,1,-4], target = 1
# 输出：2
# 解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2)。

# 示例 2：
# 输入：nums = [0,0,0], target = 1
# 输出：0
# 解释：与 target 最接近的和是 0（0 + 0 + 0 = 0）。
 
# 提示：
# 3 <= nums.length <= 1000
# -1000 <= nums[i] <= 1000
# -104 <= target <= 104

from math import abs

class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        ans=2**31-1
        n=len(nums)
        nums.sort()
        
        for i in range(n):
            if i>0 and nums[i]==nums[i-1]:
                continue
            l,r=i+1,len(nums)-1
            while l<r:
                summary = nums[i]+nums[l]+nums[r]
                if summary==target:
                    return summary
                if abs(target-summary)<abs(target-ans):
                    ans=summary
                if summary<target:
                    l+=1
                else:
                    r-=1
        return ans