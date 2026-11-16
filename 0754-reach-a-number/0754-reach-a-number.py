class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        n = int(ceil((sqrt(8 * target + 1) - 1) / 2))
        s = n * (n + 1) // 2
        return n if not (s - target) % 2 else n + 2 - (n + 1) % 2

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna