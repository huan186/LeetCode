class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        res = float('-inf')
        for i in range(1, len(grid) - 1):
            for j in range(1, len(grid[0]) - 1):
                res = max(res, grid[i][j])
        def max_score(g):
            nonlocal res
            for row in g:
                curr = row[0] + row[1]
                res = max(res, curr)
                for i in range(2, len(row)):
                    curr = max(curr + row[i], row[i - 1] + row[i])
                    res = max(res, curr)
        max_score(grid)
        max_score(list(zip(*grid)))
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna