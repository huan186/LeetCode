class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def p(x):
            product = 1
            while x > 0:
                product *= x % 10
                x //= 10
            return product
        while True:
            if p(n) % t == 0:
                return n
            n += 1

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna