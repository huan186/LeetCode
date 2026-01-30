class Solution:
    def numOfSubsequences(self, s: str) -> int:
        n = len(s)
        pref = [[0] * 3 for _ in range(n + 1)]
        for i in range(n):
            pref[i + 1][0] = pref[i][0] + (s[i] == 'L')
            pref[i + 1][1] = pref[i][1] + (s[i] == 'C')
            pref[i + 1][2] = pref[i][2] + (s[i] == 'T')

        base_LCT = 0
        gain_insert_L = 0
        gain_insert_T = 0
        gain_insert_C = 0

        for i in range(n):
            if s[i] == 'C':
                L_before = pref[i][0]
                T_after = pref[n][2] - pref[i + 1][2]
                base_LCT += L_before * T_after
                gain_insert_L += T_after
                gain_insert_T += L_before
            gain_insert_C = max(
                gain_insert_C,
                pref[i + 1][0] * (pref[n][2] - pref[i + 1][2])
            )

        return base_LCT + max(gain_insert_L, gain_insert_C, gain_insert_T)
