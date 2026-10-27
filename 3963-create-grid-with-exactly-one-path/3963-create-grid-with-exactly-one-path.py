class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        res = ['.' * n]
        res += ['#' * (n - 1) + '.'] * (m - 1)
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna