class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        f = [-1] * 26
        l = [-1] * 26
        for i, c in enumerate(word):
            if c.isupper():
                j = ord(c) - ord('A')
                if f[j] == -1:
                    f[j] = i
            else:
                j = ord(c) - ord('a')
                l[j] = i
        return sum(0 <= l[i] < f[i] for i in range(26))

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna