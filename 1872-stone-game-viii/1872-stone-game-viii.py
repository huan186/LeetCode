class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        n = len(stones)
        f = s = sum(stones)
        for i in range(n - 2, 0, -1):
            s -= stones[i + 1]
            f = max(f, s - f)
        return f

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna