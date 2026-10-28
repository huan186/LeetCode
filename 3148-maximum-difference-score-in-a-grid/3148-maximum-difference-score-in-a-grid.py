class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        p = [inf] * (len(grid[0]) + 1)
        res = -inf
        for row in grid:
            for i, v in enumerate(row):
                m = min(p[i], p[i + 1])
                p[i + 1] = min(v, m)
                res = max(res, v - m)
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna