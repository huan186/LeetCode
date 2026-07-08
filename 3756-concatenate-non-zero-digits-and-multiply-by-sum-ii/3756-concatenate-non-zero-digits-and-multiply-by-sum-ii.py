class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        mod = 10 ** 9 + 7
        a, b, c = [0], [0], [0]
        for ch in s:
            if ch == '0':
                a.append(a[-1])
                b.append(b[-1])
                c.append(c[-1])
            else:
                d = int(ch)
                a.append((a[-1] * 10 + d) % mod)
                b.append(b[-1] + d)
                c.append(c[-1] + 1)
        res = []
        for l, r in queries:
            x = b[r + 1] - b[l]
            y = (a[r + 1] - a[l] * pow(10, c[r + 1] - c[l], mod)) % mod
            res.append((x * y) % mod)
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna