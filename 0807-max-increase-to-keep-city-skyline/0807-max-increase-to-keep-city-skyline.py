class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)
        largest_in_row = [0] * n
        largest_in_col = [0] * n
        for i in range(n):
            for j in range(n):
                largest_in_row[i] = max(largest_in_row[i], grid[i][j])
                largest_in_col[j] = max(largest_in_col[j], grid[i][j])
        res = 0
        for i in range(n):
            for j in range(n):
                res += min(largest_in_row[i], largest_in_col[j]) - grid[i][j]
        return res