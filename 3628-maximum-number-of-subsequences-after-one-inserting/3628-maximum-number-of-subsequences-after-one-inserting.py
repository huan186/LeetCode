class Solution:
    def numOfSubsequences(self, s: str) -> int:
        n = len(s)
        ps = [[0] * 3 for _ in range(n + 1)] # prefix sum
        for i in range(n):
            ps[i + 1][0] = ps[i][0] + (1 if s[i] == 'L' else 0)
            ps[i + 1][1] = ps[i][1] + (1 if s[i] == 'C' else 0)
            ps[i + 1][2] = ps[i][2] + (1 if s[i] == 'T' else 0)
        cnt = 0
        gain_L = 0 # inset a L at 0
        max_gain_C = 0 # insert a T at n
        gain_T = 0
        for i in range(n):
            if s[i] == 'C':
                cnt += ps[i][0] * (ps[n][2] - ps[i + 1][2])
                gain_L += ps[i][0]
                gain_T += ps[n][2] - ps[i + 1][2]
            max_gain_C = max(
                max_gain_C,
                ps[i + 1][0] * (ps[n][2] - ps[i + 1][2]) # insert a C at i + 1
            )
        return cnt + max(gain_L, max_gain_C, gain_T)