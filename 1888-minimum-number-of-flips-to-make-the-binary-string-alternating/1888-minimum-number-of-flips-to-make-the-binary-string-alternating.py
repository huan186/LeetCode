class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            dp[i] = dp[i + 1] + (i % 2 == int(s[i]))
        ans = min(dp[0], n - dp[0])
        if n % 2 == 0:
            return ans
        flips = 0
        for i, c in enumerate(s):
            if i % 2 != int(c):
                flips += 1
            f = flips + dp[i + 1]
            ans = min(ans, f, n - f)
        return ans
