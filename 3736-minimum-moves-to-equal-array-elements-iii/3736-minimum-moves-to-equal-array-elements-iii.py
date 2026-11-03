class Solution:
    def minMoves(self, nums: List[int]) -> int:
        m = max(nums)
        return sum(m - x for x in nums)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna