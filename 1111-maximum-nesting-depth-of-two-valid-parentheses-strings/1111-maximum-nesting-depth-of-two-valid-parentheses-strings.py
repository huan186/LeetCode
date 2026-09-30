class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        return [(c == ')') ^ (i % 2) for i, c in enumerate(seq)]


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna