class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 3:
            return 0
        nums.sort()
        return min(nums[-3 + i] - nums[i] for i in range(3))

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna