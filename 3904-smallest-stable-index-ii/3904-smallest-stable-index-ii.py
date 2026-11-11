class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        mx = [nums[0]] * n
        mn = [nums[-1]] * n
        for i in range(1, n):
            mx[i] = max(mx[i - 1], nums[i])
            mn[-i - 1] = min(mn[-i], nums[-i - 1])
        for i in range(n):
            if mx[i] - mn[i] <= k:
                return i
        return -1

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna