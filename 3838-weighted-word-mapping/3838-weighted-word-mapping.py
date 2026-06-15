class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        res = ''
        for word in words:
            w = 0
            for c in word:
                w += weights[ord(c) - ord('a')]
            w %= 26
            res += chr(ord('z') - w)
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna