class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        dp = [[0] * n for _ in range(m)]

        for c in range(n - 2, -1, -1):
            for r in range(m):
                for nr in (r - 1, r, r + 1):
                    if 0 <= nr < m and grid[nr][c + 1] > grid[r][c]:
                        dp[r][c] = max(dp[r][c], 1 + dp[nr][c + 1])

        return max(dp[r][0] for r in range(m))

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna