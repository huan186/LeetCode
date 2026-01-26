class Solution:
    def binaryGap(self, n: int) -> int:
        if n & n - 1 == 0:
            return 0
        res, cnt = 0, 0
        for ch in str(bin(n)[2:]):
            if ch == '1':
                res = max(res, cnt)
                cnt = 1
            else:
                cnt += 1
        return res