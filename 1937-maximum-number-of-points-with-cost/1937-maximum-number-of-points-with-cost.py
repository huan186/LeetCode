class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points[0])
        dp = [0] * n
        for row in points:
            x = 0
            for i in range(n):
                dp[i] = max(dp[i], x)
                x = dp[i] - 1
            x = 0
            for i in range(n - 1, -1, -1):
                dp[i] = max(dp[i], x)
                x = dp[i] - 1
            for i in range(n):
                dp[i] += row[i]
        return max(dp)