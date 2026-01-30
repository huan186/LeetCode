class Solution:
    def numOfSubsequences(self, s: str) -> int:
        total_T = s.count('T')

        L_cnt = 0
        LC_cnt = 0
        base_LCT = 0

        gain_insert_C = 0
        gain_insert_L = 0
        gain_insert_T = 0

        T_remaining = total_T

        for ch in s:
            if ch == 'L':
                L_cnt += 1
            elif ch == 'C':
                base_LCT += L_cnt * T_remaining
                LC_cnt += L_cnt
                gain_insert_L += T_remaining
                gain_insert_T += L_cnt
            elif ch == 'T':
                T_remaining -= 1

            gain_insert_C = max(gain_insert_C, L_cnt * T_remaining)

        return base_LCT + max(gain_insert_L, gain_insert_C, gain_insert_T)
