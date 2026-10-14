class Solution:
    def maxSumOfSquares(self, num: int, s: int) -> str:
        if 9 * num < s:
            return ''
        res = ''
        for d in range(9, 0, -1):
            cnt = s // d
            s %= d
            num -= cnt
            res += str(d) * cnt
        res += '0' * num
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna