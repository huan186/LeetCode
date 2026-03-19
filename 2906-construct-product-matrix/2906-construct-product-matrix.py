class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        mod = 12345
        m, n = len(grid), len(grid[0])
        left = [[1] * n for _ in range(m)]
        right = [[1] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == j == 0:
                    continue
                pi, pj = (i, j - 1) if j > 0 else (i - 1, n - 1)
                left[i][j] = (left[pi][pj] * grid[pi][pj]) % mod
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i == m - 1 and j == n - 1:
                    continue
                ni, nj = (i, j + 1) if j < n - 1 else (i + 1, 0)
                right[i][j] = (right[ni][nj] * grid[ni][nj]) % mod
        res = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                res[i][j] = (left[i][j] * right[i][j]) % mod
        return res