class Solution:
    def binaryGap(self, n: int) -> int:
        if n & n - 1 == 0:
            return 0
        res = 0
        while n > 0:
            cnt = 1
            while n & 1 != 1:
                n >>= 1
                cnt += 1
            res = max(res, cnt)
            n >>= 1
        return res