class Solution:
    def matrixBlockSum(self, mat, k):
        m, n = len(mat), len(mat[0])
        ps = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                ps[i + 1][j + 1] = mat[i][j] + ps[i][j + 1] + ps[i + 1][j] - ps[i][j]

        res = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                r1, r2 = max(0, i - k), min(m, i + k + 1)
                c1, c2= max(0, j - k), min(n, j + k + 1)
                res[i][j] = ps[r2][c2] - ps[r1][c2] - ps[r2][c1] + ps[r1][c1]

        return res