class Solution:
    def sumAndMultiply(self, n: int) -> int:
        x = str(n).replace("0", "")
        if not x:
            return 0
        return int(x) * sum(map(int, x))

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna