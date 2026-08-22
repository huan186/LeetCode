class Solution:
    def checkDivisibility(self, n: int) -> bool:
        a = list(map(int, str(n)))
        return n % (sum(a) + prod(a)) == 0

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna