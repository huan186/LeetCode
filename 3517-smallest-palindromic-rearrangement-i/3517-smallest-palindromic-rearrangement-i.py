class Solution:
    def smallestPalindrome(self, s: str) -> str:
        f = Counter(s)
        r = []
        mid = ''
        for ch, c in sorted(f.items()):
            r.extend([ch] * (c // 2))
            if c & 1:
                mid = ch
        return ''.join(r + [mid] + r[::-1])

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna