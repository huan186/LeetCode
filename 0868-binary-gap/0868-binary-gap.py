class Solution:
    def binaryGap(self, n: int) -> int:
        if n & n - 1 == 0:
            return 0
        while n & 1 == 0:
            n >>= 1
        res, cnt = 0, 0
        while n > 0:
            if n & 1 == 1:
                res = max(res, cnt)
                cnt = 1
            else:
                cnt += 1
            n >>= 1
        return res