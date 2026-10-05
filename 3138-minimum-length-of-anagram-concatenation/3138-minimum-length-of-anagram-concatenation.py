from math import gcd, sqrt

class Solution:
    def minAnagramLength(self, s: str) -> int:
        n = len(s)

        f = [[0] * 26 for _ in range(n + 1)]
        for i, c in enumerate(s):
            f[i + 1] = f[i].copy()
            f[i + 1][ord(c) - ord('a')] += 1

        g = f[-1][ord(s[0]) - ord('a')]
        for x in f[-1]:
            if x:
                g = gcd(g, x)

        min_l = n // g

        def valid(l):
            target = [x // (n // l) for x in f[-1]]

            for i in range(0, n, l):
                for j in range(26):
                    if f[i + l][j] - f[i][j] != target[j]:
                        return False

            return True

        for l in range(min_l, n + 1, min_l):
            if n % l == 0 and valid(l):
                return l

        return n

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna