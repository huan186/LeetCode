class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        def product(i, j, k):
            return nums[i] * nums[j] * nums[k]
        return max(
            product(0, 1, -1),
            product(-1, -2, -3),
        )

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna