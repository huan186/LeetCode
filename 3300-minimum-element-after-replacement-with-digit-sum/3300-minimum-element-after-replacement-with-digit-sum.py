class Solution:
    def minElement(self, nums: List[int]) -> int:
        return min(sum(map(int, str(num))) for num in nums)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna