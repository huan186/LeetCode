class Solution:
    def binaryGap(self, n: int) -> int:
        last = -1
        res = 0
        for i in range(32):
            if n & 1:
                if last != -1:
                    res = max(res, i - last)
                last = i
            n >>= 1
        return res