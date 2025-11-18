# 给你两个整数，被除数 dividend 和除数 divisor。将两数相除，要求 不使用 乘法、除法和取余运算。
# 整数除法应该向零截断，也就是截去（truncate）其小数部分。例如，8.345 将被截断为 8 ，-2.7335 将被截断至 -2 。
# 返回被除数 dividend 除以除数 divisor 得到的 商 。

# 注意：假设我们的环境只能存储 32 位 有符号整数，其数值范围是 [−231,  231 − 1] 。
# 本题中，如果商 严格大于 231 − 1 ，则返回 231 − 1 ；如果商 严格小于 -231 ，则返回 -231 。

# 示例 1:
# 输入: dividend = 10, divisor = 3
# 输出: 3
# 解释: 10/3 = 3.33333.. ，向零截断后得到 3 。

# 示例 2:
# 输入: dividend = 7, divisor = -3
# 输出: -2
# 解释: 7/-3 = -2.33333.. ，向零截断后得到 -2 。

# 提示：
# -2^31 <= dividend, divisor <= 2^31 - 1
# divisor != 0

class Solution:
    def divide(self, divided: int, divisor: int) -> int:
        if divided==0: return 0

        INT_MIN, INT_MAX = -2**31, 2**31-1

        if divisor==1:
            if divided < INT_MIN: return INT_MIN
            elif divided > INT_MAX: return INT_MAX
            else: return divided
        if divisor==-1:
            if divided <= INT_MIN: return INT_MAX
            elif divided > INT_MAX: return INT_MIN
            else: return -divided

        flag = (divided>0)==(divisor>0)
        divided, divisor = abs(divided), abs(divisor)
        ans=0
        
        while divided >= divisor:
            tmp, count = divisor,1
            while divided >= (tmp<<1):
                tmp<<=1
                count<<=1
            divided-=tmp
            ans+=count
        
        if not flag:
            ans=-ans
        
        return min(max(INT_MIN,ans),INT_MAX)