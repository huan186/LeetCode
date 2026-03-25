class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        sum_row = [0] * m
        sum_col = [0] * n
        total = 0
        for i in range(m):
            for j in range(n):
                sum_row[i] += grid[i][j]
                sum_col[j] += grid[i][j]
                total += grid[i][j]

        def can_divide(arr):
            curr_sum = 0
            for i in range(len(arr) - 1):
                curr_sum += arr[i]
                if (curr_sum << 1) == total:
                    return True
            return False
        
        return can_divide(sum_row) or can_divide(sum_col)