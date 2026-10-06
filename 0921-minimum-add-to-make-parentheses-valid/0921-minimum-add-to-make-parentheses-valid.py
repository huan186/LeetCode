class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        res = 0
        d = 0
        for c in s:
            if c == '(':
                d += 1
            elif d == 0:
                res += 1
            else:
                d -= 1
        return res + d

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna