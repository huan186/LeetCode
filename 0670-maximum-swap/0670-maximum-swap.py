class Solution:
    def maximumSwap(self, num: int) -> int:
        s = str(num)
        res = num
        n = len(s)
        for i in range(n - 1):
            for j in range(i + 1, n):
                v = int(s[:i] + s[j] + s[i + 1:j] + s[i] + s[j + 1:])
                res = max(res, v)
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna