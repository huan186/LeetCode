class Solution:
    def canAliceWin(self, n: int) -> bool:
        x = 10
        while n >= x:
            if n < 2 * x - 1:
                return True
            n -= 2 * x - 1
            x -= 2
        return False

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna