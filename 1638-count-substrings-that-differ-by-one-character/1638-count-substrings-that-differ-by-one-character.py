class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        m, n = len(s), len(t)

        dpL = [[0] * (n + 1) for _ in range(m + 1)]
        dpR = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m):
            for j in range(n):
                if s[i] == t[j]:
                    dpL[i + 1][j + 1] = dpL[i][j] + 1

        for i in reversed(range(m)):
            for j in reversed(range(n)):
                if s[i] == t[j]:
                    dpR[i][j] = dpR[i + 1][j + 1] + 1

        res = 0

        for i in range(m):
            for j in range(n):
                if s[i] != t[j]:
                    res += (dpL[i][j] + 1) * (dpR[i + 1][j + 1] + 1)
        
        return res