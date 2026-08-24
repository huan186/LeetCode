class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        n = len(stones)
        s = list(accumulate(stones))
        f = [0] * n
        f[-1] = s[-1]
        for i in range(n - 2, 0, -1):
            f[i] = max(f[i + 1], s[i] - f[i + 1])
        return f[1]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna