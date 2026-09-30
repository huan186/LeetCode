class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        res = []
        depth = 0

        for c in seq:
            if c == '(':
                res.append(depth & 1)
                depth += 1
            else:
                depth -= 1
                res.append(depth & 1)

        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna