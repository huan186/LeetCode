class Solution:
    def findMin(self, nums: List[int]) -> int:
        def helper(left, right):
            if nums[left] <= nums[right]:
                return nums[left]

            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                return helper(mid + 1, right)
            return helper(left, mid)

        return helper(0, len(nums) - 1)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna