class Solution:
    def minimumSwaps(self, nums: list[int]) -> int:
        n = len(nums)
        zero = nums.count(0)
        return zero - nums[n - zero:].count(0)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna