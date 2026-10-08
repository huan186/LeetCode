class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res = []
        d = 0
        for c in s:
            a = c == '('
            res.append('' if d == (0 if a else 1) else c)
            d += 1 if a else -1
        return ''.join(res)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna