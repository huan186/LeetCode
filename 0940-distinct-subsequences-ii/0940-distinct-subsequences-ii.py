class Solution:
    def distinctSubseqII(self, s: str) -> int:
        mod = int(1e9 + 7)
        res = 0
        dp = [0] * 26
        for c in s:
            i = ord(c) - ord('a')
            dp[i], res = res + 1, (2 * res + 1 - dp[i]) % mod
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna