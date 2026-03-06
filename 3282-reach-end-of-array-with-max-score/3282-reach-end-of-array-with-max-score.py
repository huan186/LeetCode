class Solution:
    def findMaximumScore(self, nums: List[int]) -> int:
        prev_idx, n = 0, len(nums)
        res = 0
        for idx in range(1, n):
            if nums[idx] > nums[prev_idx]:
                res += nums[prev_idx] * (idx - prev_idx)
                prev_idx = idx
        res += (n - 1 - prev_idx) * nums[prev_idx]
        return res
