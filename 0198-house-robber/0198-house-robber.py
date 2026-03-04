class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        prev2, prev1 = 0, 0
        for num in nums:
            prev1, prev2 = max(prev1, prev2 + num), prev1
        return prev1