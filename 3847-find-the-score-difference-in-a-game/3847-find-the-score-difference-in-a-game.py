class Solution:
    def scoreDifference(self, nums: List[int]) -> int:
        diff = 0
        sign = 1
        for i, num in enumerate(nums):
            if (nums[i] % 2) ^ (i % 6 == 5):
                sign *= -1
            diff += num * sign
        return diff