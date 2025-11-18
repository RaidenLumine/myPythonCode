class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        been = dict()
        maxLen = left = 0
        for right in range(len(s)):
            cur = s[right]
            if cur in been and been[cur] >= left:
                left = been[cur] + 1
            been[cur] = right
            maxLen = max(maxLen, right - left + 1)
        return maxLen