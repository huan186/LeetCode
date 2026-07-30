class Solution:
    def minimumPushes(self, A: str) -> int:
        q, r = divmod(len(A), 8)
        return ((q << 2) + r) * (q + 1)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna