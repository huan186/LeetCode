class Solution:
    def findNthDigit(self, n: int) -> int:
        total = 0
        l = 1

        while total + l * 9 * 10 ** (l - 1) < n:
            total += l * 9 * 10 ** (l - 1)
            l += 1

        r = n - total - 1
        x = 10 ** (l - 1) + r // l
        y = r % l
        return int(str(x)[y])

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna