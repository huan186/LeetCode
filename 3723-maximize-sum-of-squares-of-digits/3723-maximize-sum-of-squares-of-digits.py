class Solution:
    def maxSumOfSquares(self, num: int, s: int) -> str:
        if 9 * num < s:
            return ''
        a, b = divmod(s, 9)
        res = '9' * a
        if b > 0:
            res += str(b)
        res += '0' * (num - len(res))
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna