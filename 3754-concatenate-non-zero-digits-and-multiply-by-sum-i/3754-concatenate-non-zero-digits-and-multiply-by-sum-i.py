class Solution:
    def sumAndMultiply(self, n: int) -> int:
        if not n:
            return 0
        s = 0
        x = ""
        while n:
            d = n % 10
            n //= 10
            if not d:
                continue
            x = str(d) + x
            s += d
        return int(x) * s

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna