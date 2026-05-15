class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return inf
        if n == 1 or nums[0] < nums[-1]:
            return nums[0]
        mid = n // 2
        return min(self.findMin(nums[:mid]), self.findMin(nums[mid:]))


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna