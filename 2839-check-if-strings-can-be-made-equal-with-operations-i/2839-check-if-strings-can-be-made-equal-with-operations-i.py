class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        def valid(i):
            a, b, c, d = s1[i], s1[i + 2], s2[i], s2[i + 2]
            return a == c and b == d or a == d and b == c
        return valid(0) and valid(1)