class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        res = cnt = sum(s[i] in vowels for i in range(k))
        for i in range(k, len(s)):
            cnt += (s[i] in vowels) - (s[i - k] in vowels)
            res = max(res, cnt)
        return res
            

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna