class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        total = sum(nums)
        s = 0
        res = inf
        n = len(nums)
        for i in range(n):
            s += nums[i]
            res = min(res, nums[i] * (2 * i + 2 - n) + (total - 2 * s))
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna