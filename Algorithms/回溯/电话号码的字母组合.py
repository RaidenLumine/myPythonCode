# 给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按任意顺序返回。
# 注意 1 不对应任何字母。

# 示例 1：
# 输入：digits = "23"
# 输出：["ad","ae","af","bd","be","bf","cd","ce","cf"]

# 示例 2：
# 输入：digits = ""
# 输出：[]

# 示例 3：
# 输入：digits = "2"
# 输出：["a","b","c"]

# 提示：
# 0 <= digits.length <= 4
# digits[i] 是范围 ['2', '9'] 的一个数字。

class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []
        
        Map = {
            '2':"abc",
            '3':"def",
            '4':"ghi",
            '5':"jkl",
            '6':"mno",
            '7':"pqrs",
            '8':"tuv",
            '9':"wxyz"
        }

        res = []
        
        def backtrack(index, path):
            if index == len(digits):
                res.append(path)
                return
            for char in Map[digits[index]]:
                backtrack(index + 1, path + char)
                
        backtrack(0, "")
        return res