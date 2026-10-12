class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        v = set('aeiou')
        cnt = res = sum(c in v for c in s[:k])

        for i in range(k, len(s)):
            cnt += (s[i] in v) - (s[i-k] in v)
            res = max(res, cnt)
            if res == k:
                return k

        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna