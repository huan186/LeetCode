class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lowers = set(c for c in word if c.islower())
        uppers = set(c.lower() for c in word if c.isupper())
        return len(lowers.intersection(uppers))

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna