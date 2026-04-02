class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        m, n = len(coins), len(coins[0])
        inf = - 10 ** 18
        dp = [[[inf] * 3 for _ in range(n)] for _ in range(m)]

        def dfs(row, col, k: int) -> int:
            if dp[row][col][k] != inf:
                return dp[row][col][k]
            profit = inf
            if row == m - 1 and col == n - 1:
                if coins[-1][-1] < 0 < k:
                    profit = 0
                else:
                    profit = coins[-1][-1]
            else:
                for dr, dc in ((1, 0), (0, 1)):
                    nr, nc = row + dr, col + dc
                    if nr >= m or nc >= n:
                        continue
                    profit = max(profit, coins[row][col] + dfs(nr, nc, k))
                    if coins[row][col] < 0 < k:
                        profit = max(profit, dfs(nr, nc, k - 1))
            dp[row][col][k] = profit
            return profit

        return dfs(0, 0, 2)