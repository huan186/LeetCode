class Solution:
    def countCommas(self, n: int) -> int:
        a = 1
        b = 1000
        commas = 0
        res = 0
        while n >= a:
            if n < b:
                res += (n - a + 1) * commas
                break
            else:
                res += (b - a) * commas
                a, b = b, b * 1000
                commas += 1
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna