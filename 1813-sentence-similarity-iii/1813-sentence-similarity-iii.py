class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        a = sentence1.split()
        b = sentence2.split()

        if len(a) > len(b):
            a, b = b, a

        i = 0
        while i < len(a) and a[i] == b[i]:
            i += 1

        j = 0
        while j < len(a) - i and a[len(a) - 1 - j] == b[len(b) - 1 - j]:
            j += 1

        return i + j == len(a)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna