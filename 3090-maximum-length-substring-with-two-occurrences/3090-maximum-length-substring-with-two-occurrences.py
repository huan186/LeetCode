class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        res = 0
        l = 0
        f = defaultdict(int)
        for r in range(len(s)):
            f[s[r]] += 1
            while f[s[r]] > 2:
                f[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna