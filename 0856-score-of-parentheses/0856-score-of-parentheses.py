class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        res = 0
        d = 1
        for i in range(1, len(s)):
            if s[i] == '(':
                d += 1
            else:
                d -= 1
                if s[i] != s[i - 1]:
                    res += 1 << d
        return res


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna