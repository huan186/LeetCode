class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                dp[i + 1][j + 1] = mat[i][j] + dp[i + 1][j]
            for j in range(n):
                dp[i + 1][j + 1] += dp[i][j + 1]

        def calculate_sum(t, b, l, r):
            t, b = max(t, 0), min(b, m - 1)
            l, r = max(l, 0), min(r, n - 1)
            return dp[b + 1][r + 1] + dp[t][l] - dp[b + 1][l] - dp[t][r + 1]
        
        res = [[0] * n for _ in range(m)]

        for i in range(m):
            top, bottom = i - k, i + k
            for j in range(n):
                left, right = j - k, j + k
                res[i][j] = calculate_sum(top, bottom, left, right)
        return res