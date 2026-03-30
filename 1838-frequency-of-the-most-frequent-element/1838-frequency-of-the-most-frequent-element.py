class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        i, j = n - 1, n - 2
        res = 1
        while i > 0 and j >= 0:
            while j >= 0 and k >= 0 and nums[i] - nums[j] <= k:
                k -= nums[i] - nums[j]
                j -= 1
            cnt = i - j
            res = max(res, cnt)
            k += (cnt - 1) * (nums[i] - nums[i - 1])
            i -= 1
        return res