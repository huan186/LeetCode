class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        rc = [0] * m
        cc = [0] * n
        for r in range(m):
            for c in range(n):
                if grid[r][c]:
                    rc[r] += 1
                    cc[c] += 1
        res = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] and (rc[r] > 1 or cc[c] > 1):
                    res += 1
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna