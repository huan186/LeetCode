class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points[0])
        dp = [0] * n
        for row in points:
            for start, end, step in ((0, n, 1), (n - 1, -1, -1)):
                x = 0
                for i in range(start, end, step):
                    dp[i] = max(dp[i], x)
                    x = dp[i] - 1
            for i in range(n):
                dp[i] += row[i]
        return max(dp)