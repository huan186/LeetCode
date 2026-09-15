class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        pal = [[False] * n for _ in range(n)]
        dp = [0] * (n + 1)

        for i in range(n):
            pal[i][i] = True

        for j in range(n):
            for i in range(j + 1):
                if s[i] == s[j]:
                    pal[i][j] = j - i < 2 or pal[i + 1][j - 1]

                dp[j + 1] = max(dp[j + 1], dp[j])
                if j - i + 1 >= k and pal[i][j]:
                    dp[j + 1] = max(dp[j + 1], dp[i] + 1)

        return dp[n]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna