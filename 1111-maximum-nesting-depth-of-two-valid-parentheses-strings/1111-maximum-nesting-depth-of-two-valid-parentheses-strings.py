class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        res = []
        depth = 0
        for c in seq:
            if c == '(':
                res.append(depth % 2)
                depth += 1
            else:
                res.append(1 - depth % 2)
                depth -= 1
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna