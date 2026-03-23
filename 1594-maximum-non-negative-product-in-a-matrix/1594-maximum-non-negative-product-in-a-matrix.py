class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        mod = 10 ** 9 + 7
        m, n = len(grid), len(grid[0])
        dp = [[grid[0][0]]]
        for i in range(1, n):
            dp.append([dp[-1][0] * grid[0][i]])
        for i in range(1, m):
            nxt_dp = [[x * grid[i][0] for x in dp[0]]]
            for j in range(1, n):
                num = grid[i][j]
                v = set()
                for x in nxt_dp[-1] + dp[j]:
                    v.add(x * num)
                nxt = []
                if min(v) < 0:
                    nxt.append(min(v))
                if max(v) > 0:
                    nxt.append(max(v))
                if 0 in v:
                    nxt.append(0)
                nxt_dp.append(nxt)
            dp = nxt_dp
        return -1 if max(dp[-1]) < 0 else max(dp[-1]) % mod