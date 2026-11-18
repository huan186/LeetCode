class Solution:
    def minChanges(self, s: str) -> int:
        return sum(s[2 * i] != s[2 * i + 1] for i in range(len(s) // 2))

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna