class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        flips = 0
        if n % 2 == 0:
            for i, c in enumerate(s):
                if i % 2 != int(c):
                    flips += 1
            return min(flips, n - flips)
        dp = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            dp[i] = dp[i + 1] + (1 if i % 2 == int(s[i]) else 0)
        ans = min(dp[0], n - dp[0])
        flips = 0
        for i, c in enumerate(s):
            if i % 2 != int(c):
                flips += 1
            f = flips + dp[i + 1]
            ans = min(ans, f, n - f)
        return ans