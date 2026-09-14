class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        f1, f2 = Counter(word1), Counter(word2)
        for i in range(26):
            c = chr(ord('a') + i)
            if (c in f1) ^ (c in f2):
                return False
        v1, v2 = list(sorted(f1.values())), list(sorted(f2.values()))
        for e1, e2 in zip(v1, v2):
            if e1 != e2:
                return False
        return True

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna