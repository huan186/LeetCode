class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if target > sum(nums):
            return 0
        total = 0
        left = 0
        res = len(nums)
        for right in range(len(nums)):
            total += nums[right]
            while total - nums[left] >= target:
                total -= nums[left]
                left += 1
                res = min(res, right - left + 1)
                
        return res