class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        ops = 0 
        median = nums[len(nums)//2] 
        for i in nums: 
            ops += abs(i-median) 
        return ops

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna