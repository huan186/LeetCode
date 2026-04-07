class Solution:
    def minimumCost(self, nums, cost, k):
        a = list(accumulate(nums, initial=0))
        c = list(accumulate(cost, initial=0))
        n = len(nums)

        @lru_cache(None)
        def dp(i):
            if i == n:
                return 0
            return min(a[j + 1] * (c[j + 1] - c[i]) + k * (c[-1] - c[i]) + dp(j + 1) for j in range(i, n))

        return dp(0)