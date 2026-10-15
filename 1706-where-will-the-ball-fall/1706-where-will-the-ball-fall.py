class Solution:
    def findBall(self, grid: list[list[int]]) -> list[int]:
        m, n = len(grid), len(grid[0])
        def solve(i, j):
            if grid[i][j] == 1:
                if j == n - 1 or grid[i][j + 1] == -1:
                    return -1
                if i == m - 1:
                    return j + 1
                return solve(i + 1, j + 1)
            else:
                if j == 0 or grid[i][j - 1] == 1:
                    return -1
                if i == m - 1:
                    return j - 1
                return solve(i + 1, j - 1)
        return [solve(0, c) for c in range(n)]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna