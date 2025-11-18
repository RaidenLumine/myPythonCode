# 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且有效的括号组合。

# 示例 1：
# 输入：n = 3
# 输出：["((()))","(()())","(())()","()(())","()()()"]

# 示例 2：
# 输入：n = 1
# 输出：["()"]

# 提示：
# 1 <= n <= 8


class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        ans=[]
        path=['']*(n*2)
        
        def backtrack(left:int, right:int)->None:
            if right == n:  # 填完
                ans.append(''.join(path))
                return
            if left < n:    # 可填 （
                path[left+right]='('
                backtrack(left+1,right)
            if right < left:    # 可填 ）
                path[left+right]=')'
                backtrack(left,right+1)

        backtrack(0,0)

        return ans