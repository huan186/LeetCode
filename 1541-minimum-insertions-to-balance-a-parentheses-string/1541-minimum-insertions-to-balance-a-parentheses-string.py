class Solution:
    def minInsertions(self, s: str) -> int:
        res = left = 0
        i = 0

        while i < len(s):
            if s[i] == '(':
                left += 1
                i += 1
            else:
                if i + 1 < len(s) and s[i + 1] == ')':
                    i += 2
                else:
                    res += 1
                    i += 1

                if left:
                    left -= 1
                else:
                    res += 1

        return res + 2 * left

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna