class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        cnt = 0
        res = 0
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        for i in range(len(s)):
            cnt += s[i] in vowels
            if i < k - 1:
                continue
            res = max(res, cnt)
            cnt -= s[i - k + 1] in vowels
        return res
            

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna