class Solution:
    def minimumDeletions(self, s: str) -> int:
        a, b = s.count('a'), 0
        res = a
        for ch in s:
            res = min(res, a + b)
            if ch == 'a':
                a -= 1
            else:
                b += 1
        return min(res, a + b)