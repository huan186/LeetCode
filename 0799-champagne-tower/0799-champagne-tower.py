class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [poured]
        for row in range(1, query_row + 1):
            nxt = [0] * (row + 1)
            for i in range(row):
                nxt[i] += max((dp[i] - 1) / 2, 0)
                nxt[i + 1] += max((dp[i] - 1) / 2, 0)
            dp = nxt
        return min(dp[query_glass], 1)