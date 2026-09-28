class Solution:
    def maxDepth(self, s: str) -> int:
        res = 0
        cnt = 0
        for c in s:
            if c == '(':
                cnt += 1
                res = max(res, cnt)
            elif c == ')':
                cnt -= 1
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna