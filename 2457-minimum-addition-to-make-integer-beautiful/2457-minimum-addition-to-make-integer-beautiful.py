class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        original = n
        p = 1

        while sum(map(int, str(n))) > target:
            n = (n // (p * 10) + 1) * (p * 10)
            p *= 10

        return n - original

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna