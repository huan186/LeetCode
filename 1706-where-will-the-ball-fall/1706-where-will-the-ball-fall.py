
class Solution:
    def findBall(self, grid: list[list[int]]) -> list[int]:
        m, n = len(grid), len(grid[0])

        def solve(i, j):
            d = grid[i][j]
            nj = j + d

            if nj < 0 or nj >= n or grid[i][nj] != d:
                return -1

            if i == m - 1:
                return nj

            return solve(i + 1, nj)

        return [solve(0, c) for c in range(n)]


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna