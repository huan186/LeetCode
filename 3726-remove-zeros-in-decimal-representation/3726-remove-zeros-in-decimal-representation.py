class Solution:
    def removeZeros(self, n: int) -> int:
        res = 0
        for c in str(n):
            x = int(c)
            if x:
                res = 10 * res + x
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna