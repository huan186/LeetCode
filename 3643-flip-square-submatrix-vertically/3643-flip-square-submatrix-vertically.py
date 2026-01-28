class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        for col in range(y, y + k):
            row1, row2 = x, x + k - 1
            while row1 < row2:
                grid[row1][col], grid[row2][col] = grid[row2][col], grid[row1][col]
                row1 += 1
                row2 -= 1
        return grid