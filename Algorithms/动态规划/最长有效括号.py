# 给你一个只包含 '(' 和 ')' 的字符串，找出最长有效（格式正确且连续）括号 子串 的长度。
# 左右括号匹配，即每个左括号都有对应的右括号将其闭合的字符串是格式正确的，比如 "(()())"。

# 示例 1：
# 输入：s = "(()"
# 输出：2
# 解释：最长有效括号子串是 "()"

# 示例 2：
# 输入：s = ")()())"
# 输出：4
# 解释：最长有效括号子串是 "()()"

# 示例 3：
# 输入：s = ""
# 输出：0

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0
        maxLen = 0
        dp = [0] * len(s)
        for i in range(1, len(s)):
            if s[i] == ')':
                if s[i - 1] == '(':  # 形如 "...()"
                    dp[i] = (dp[i - 2] if i >= 2 else 0) + 2
                elif i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == '(':
                    idx = i - dp[i - 1] - 2
                    dp[i] = 2 + dp[i - 1] + (dp[idx] if idx >= 0 else 0)
            maxLen = max(maxLen, dp[i])
        return maxLen
    
if __name__ == "__main__":
    s = "(()"
    print(Solution().longestValidParentheses(s))