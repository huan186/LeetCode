class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        mid = nums[len(nums) // 2]
        return sum(abs(x - mid) for x in nums)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna