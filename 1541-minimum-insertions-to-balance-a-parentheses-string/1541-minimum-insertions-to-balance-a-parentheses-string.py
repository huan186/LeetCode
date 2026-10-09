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
                j = i
                while j < n and s[j] == ')':
                    j += 1
                r = 2 * c - (j - i)
                if r >= 0:
                    if r % 2:
                        res += 1
                elif r % 2:
                    res += (3 - r) // 2
                else:
                    res -= r // 2
                c = max(0, r // 2)
                i = j
        return res + c * 2


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna