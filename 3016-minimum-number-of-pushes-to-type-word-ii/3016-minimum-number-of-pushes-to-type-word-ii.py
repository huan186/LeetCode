class Solution:
    def minimumPushes(self, word: str) -> int:
        f = sorted(Counter(word).values(), reverse=True)
        return sum(f[i] * (i // 8 + 1) for i in range(len(f)))

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna