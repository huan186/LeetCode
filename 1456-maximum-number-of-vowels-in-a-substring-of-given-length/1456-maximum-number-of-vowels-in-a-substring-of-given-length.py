class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set('aeiou')
        res = cnt = sum(c in vowels for c in s[:k])
        for c1, c2 in zip(s[:-k], s[k:]):
            cnt += (c2 in vowels) - (c1 in vowels)
            res = max(res, cnt)
        return res
            

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna