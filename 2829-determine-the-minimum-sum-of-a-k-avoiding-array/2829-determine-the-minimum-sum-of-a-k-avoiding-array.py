class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        def consecutive_sum(x):
            return x * (x + 1) // 2
        half = k // 2
        if n <= half:
            return consecutive_sum(n)
        r = n - half
        return consecutive_sum(half) + r * k + consecutive_sum(r - 1)
