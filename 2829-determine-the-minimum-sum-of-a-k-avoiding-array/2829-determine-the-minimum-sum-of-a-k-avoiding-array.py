class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        half = k >> 1
        i = 1
        res = 0
        while n:
            if i <= half or i >= k:
                res += i
                n -= 1
            i += 1
        return res