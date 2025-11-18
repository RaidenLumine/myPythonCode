# 给你两个字符串 haystack 和 needle ，
# 请你在 haystack 字符串中找出 needle 字符串的第一个匹配项的下标（下标从 0 开始）。
# 如果 needle 不是 haystack 的一部分，则返回  -1 。

# 示例 1：
# 输入：haystack = "sadbutsad", needle = "sad"
# 输出：0
# 解释："sad" 在下标 0 和 6 处匹配。
# 第一个匹配项的下标是 0 ，所以返回 0 。

# 示例 2：
# 输入：haystack = "leetcode", needle = "leeto"
# 输出：-1
# 解释："leeto" 没有在 "leetcode" 中出现，所以返回 -1 。

# 提示：
# 1 <= haystack.length, needle.length <= 104
# haystack 和 needle 仅由小写英文字符组成

class Solution:
    def strStr(self, s: str, key: str) -> int:
        strLen=len(s)
        keyLen=len(key)
        
        if not key or not s or keyLen>strLen:
            return 0
        
        nex=[0]*keyLen
        # 预处理 next 数组
        for i,j in zip(range(1,strLen),range(keyLen)):
            while j>0 and key[i]!=key[j+1]:
                j=nex[j]
            if key[i]==key[j+1]:
                j+=1
            nex[i]=j
        # 匹配过程
        for i, j in zip(range(strLen),range(keyLen)):
            while j>0 and s[i]!=key[j]:
                j=nex[j]
            if s[i]==key[j]:
                j+=1
            if j==keyLen:
                return i-keyLen+1
        return -1