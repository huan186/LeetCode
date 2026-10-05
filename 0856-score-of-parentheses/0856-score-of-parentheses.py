class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        d = 0
        prev = ''
        res = 0
        for c in s:
            if c == '(':
                d += 1
            else:
                d -= 1
                if prev != c:
                    res += 1 << d
            prev = c
        return res



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna