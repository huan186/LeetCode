class Solution:
    def maxProduct(self, words: List[str]) -> int:
        def hash(s):
            r = 0
            for c in s:
                r |= 1 << ord(c) - ord('a')
            return r
        v = [hash(w) for w in words]
        l = [len(w) for w in words]
        n = len(v)
        res = 0
        for i in range(n - 1):
            for j in range(i + 1, n):
                if v[i] & v[j] == 0:
                    res = max(res, l[i] * l[j])
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna