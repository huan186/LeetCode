class Solution:
    def waysToMakeFair(self, nums: list[int]) -> int:
        right = [sum(nums[::2]), sum(nums[1::2])]
        left = [0, 0]
        res = 0

        for i, x in enumerate(nums):
            right[i & 1] -= x
            res += left[0] + right[1] == left[1] + right[0]
            left[i & 1] += x

        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna