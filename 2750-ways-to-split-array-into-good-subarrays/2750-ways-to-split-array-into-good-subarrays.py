class Solution:
    def numberOfGoodSubarraySplits(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l <= r and nums[l] != 1:
            l += 1
        if l > r:
            return 0
        while l <= r and nums[r] != 1:
            r -= 1
        if l == r:
            return 1
        mod = 10 ** 9 + 7
        res = 1
        while l < r:
            i = l + 1
            while i <= r and nums[i] != 1:
                i += 1
            res = (res * (i - l)) % mod
            l = i
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna