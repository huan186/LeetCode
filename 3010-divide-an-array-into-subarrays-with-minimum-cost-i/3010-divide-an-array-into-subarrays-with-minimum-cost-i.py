class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        a, b = 50, 50
        for i in range(1, len(nums)):
            if nums[i] < a:
                a, b = nums[i], a
            elif nums[i] < b:
                b = nums[i]
        return nums[0] + a + b