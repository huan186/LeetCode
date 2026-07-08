class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        mod = 10 ** 9 + 7
        a = [(0, 0, 0)]
        for c in s:
            d = int(c)
            a.append((
                (a[-1][0] * 10 + d) % mod if d else a[-1][0],
                a[-1][1] + d,
                a[-1][2] + (d != 0),
            ))
        res = []
        for l, r in queries:
            x = a[r + 1][1] - a[l][1]
            y = (a[r + 1][0] - a[l][0] * pow(10, a[r + 1][2] - a[l][2], mod)) % mod
            res.append((x * y) % mod)
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna