class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        def consecutive_sum(x):
            return x * (x + 1) >> 1
        half = k >> 1
        if n <= half:
            return consecutive_sum(n)
        r = n - half
        return consecutive_sum(half) + consecutive_sum(r) + r * (k - 1)