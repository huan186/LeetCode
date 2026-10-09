class Solution:
    def minInsertions(self, s: str) -> int:
        res = 0
        i, n = 0, len(s)
        c = 0
        while i < n:
            if s[i] == '(':
                c += 1
                i += 1
            else:
                d = 2 * c
                while i < n and s[i] == ')':
                    i += 1
                    d -= 1
                if d >= 0:
                    if d % 2:
                        res += 1
                elif d % 2:
                    res += (3 - d) // 2
                else:
                    res -= d // 2
                c = max(0, d // 2)
        return res + c * 2


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna