class Solution:
    def processStr(self, s: str) -> str:
        res = []
        for c in s:
            if c == '*':
                if len(res) > 0:
                    del res[-1]
            elif c == '#':
                res += res
            elif c == '%':
                res = res[::-1]
            else:
                res.append(c)
        return ''.join(res)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna