class Solution:
    def mostWordsFound(self, sentences: list[str]) -> int:
        return max(len(s.split()) for s in sentences)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna