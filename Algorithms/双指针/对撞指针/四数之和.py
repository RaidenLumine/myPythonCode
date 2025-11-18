# 给你一个由 n 个整数组成的数组 nums ，和一个目标值 target 。
# 请你找出并返回满足下述全部条件且不重复的四元组 [nums[a], nums[b], nums[c], nums[d]] 
# （若两个四元组元素一一对应，则认为两个四元组重复）：

# 0 <= a, b, c, d < n
# a、b、c 和 d 互不相同
# nums[a] + nums[b] + nums[c] + nums[d] == target

# 你可以按 任意顺序 返回答案 。

# 示例 1：
# 输入：nums = [1,0,-1,0,-2,2], target = 0
# 输出：[[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

# 示例 2：
# 输入：nums = [2,2,2,2,2], target = 8
# 输出：[[2,2,2,2]]

# 提示：
# 1 <= nums.length <= 200
# -109 <= nums[i] <= 109
# -109 <= target <= 109

class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        ans=[]
        n=len(nums)
        
        for i in range(n-3):
            x=nums[i]
            if i>0 and nums[i]==nums[i-1]:
                continue
            if x+nums[i+1]+nums[i+2]+nums[i+3]>target:
                break
            if x+nums[-1]+nums[-2]+nums[-3]<target:
                continue
            for j in range(i+1,n-2):
                y=nums[j]
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                if x+y+nums[j+1]+nums[j+2]>target:
                    break
                if x+y+nums[-1]+nums[-2]<target:
                    continue
                l,r=j+1,n-1
                while l<r:
                    summary=nums[l]+nums[r]+x+y
                    if summary==target:
                        ans.append([x,y,nums[l],nums[r]])
                        l+=1
                        r-=1
                        while l<r and nums[l]==nums[l-1]:
                            l+=1
                        while l<r and nums[r]==nums[r+1]:
                            r-=1
                    elif summary<target:
                        l+=1
                    else:
                        r-=1
        return ans