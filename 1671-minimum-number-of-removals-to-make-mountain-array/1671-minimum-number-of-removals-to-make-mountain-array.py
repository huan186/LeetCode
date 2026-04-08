class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        @cache
        def inc(i):
            max_len = 0
            for j in range(i):
                if nums[j] >= nums[i]:
                    continue
                max_len = max(max_len, inc(j))
            return max_len + 1
        n = len(nums)
        @cache
        def dec(i):
            max_len = 0
            for j in range(i + 1, n):
                if nums[j] >= nums[i]:
                    continue
                max_len = max(max_len, dec(j))
            return max_len + 1
        res = n - 2
        for i in range(1, n - 1):
            i, d = inc(i), dec(i)
            if i == 1 or d == 1:
                continue
            res = min(res, n - i - d + 1)
        return res
