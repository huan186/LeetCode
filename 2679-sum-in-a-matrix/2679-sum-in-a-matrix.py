class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        for row in nums: row.sort()
        return sum(max(col) for col in zip(*nums))

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna