class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        f = Counter(text)
        return min(f['a'], f['b'], f['l'] // 2, f['n'], f['o'] // 2)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna