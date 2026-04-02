class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        m, n = len(coins), len(coins[0])
        inf = - 10 ** 18
        dp = [[inf] * 3 for _ in range(n + 1)]
        dp[1] = [0] * 3
        for i in range(m):
            for j in range(n):
                coin = coins[i][j]
                up0, up1, up2 = dp[j + 1]
                left0, left1, left2 = dp[j]
                dp[j + 1][0] = max(up0, left0) + coin
                dp[j + 1][1] = max(up1 + coin, left1 + coin, up0, left0)
                dp[j + 1][2] = max(up2 + coin, left2 + coin, up1, left1)
        return dp[-1][-1]