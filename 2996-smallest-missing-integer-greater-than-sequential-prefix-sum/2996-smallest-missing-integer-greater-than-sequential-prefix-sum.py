class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        n = len(nums)
        res = nums[0]
        for i in range(1, n):
            if nums[i] == nums[i - 1] + 1:
                res += nums[i]
            else:
                break
        seen = set(nums)
        while res in seen:
            res += 1
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna