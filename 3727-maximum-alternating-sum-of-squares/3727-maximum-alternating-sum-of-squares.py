class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums.sort(key=abs)
        half_len = len(nums) // 2
        def cal(a):
            return sum(x ** 2 for x in a)
        return cal(nums[half_len:]) - cal(nums[:half_len])

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna