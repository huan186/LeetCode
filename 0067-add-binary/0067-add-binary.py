class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, j, m, n = 0, 0, len(a), len(b)
        carry = 0
        res = []
        while i < m or j < n:
            d1 = 0 if i >= m else int(a[m - i - 1])
            d2 = 0 if j >= n else int(b[n - j - 1])
            d = d1 + d2 + carry
            res.append(d % 2)
            carry = 1 if d > 1 else 0
            i += 1
            j += 1
        if carry == 1:
            res.append(1)
        return ''.join(map(str, res[::-1]))