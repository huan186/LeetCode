class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        mn = [nums[-1]] * n
        for i in range(n - 2, -1, -1):
            mn[i] = min(mn[i + 1], nums[i])
        mx = 0
        for i in range(n):
            mx = max(mx, nums[i])
            if mx - mn[i] <= k:
                return i
        return -1

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna