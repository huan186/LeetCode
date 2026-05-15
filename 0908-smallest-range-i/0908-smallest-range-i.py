class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        d = max(nums) - min(nums)
        return 0 if d <= 2 * k else d - 2 * k

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna