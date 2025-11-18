# 假设你去超市，只能带一个容量是 W 的背包，有 n 件物品，每件有重量 weights[i] 和价值 values[i]。
# 你想选一部分物品装入背包，保证总重量不超过 W，且总价值最高。问最大价值是多少？

class Solution:
    def solve(self, weights: list[int], values: list[int], W: int) -> int:
        n = len(weights)
        dp = [[0]*(W+1) for _ in range(n+1)]
        
        for i in range(1,n+1):
            for j in range(W+1):
                if j < weights[i-1]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-weights[i-1]] + values[i-1])
                    
        return dp[n][W]
    
def main():
    weights = [2, 3, 4, 5]
    values = [3, 4, 5, 6]
    W = 5
    solution = Solution()
    max_value = solution.solve(weights, values, W)
    print("最大价值:", max_value)

if __name__ == "__main__":
    main()