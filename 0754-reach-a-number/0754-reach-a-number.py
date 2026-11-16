class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        n = ceil((sqrt((target << 3) + 1) - 1) / 2)
        s = n * (n + 1) >> 1
        return n + 1 + (n & 1) if (s - target) % 2 else n

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna