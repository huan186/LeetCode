class Solution:
    def splitArray(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        sl = nums[i]
        while i < n - 1 and nums[i + 1] > nums[i]:
            i += 1
            sl += nums[i]

        j = n - 1
        sr = nums[j]
        while j > 0 and nums[j - 1] > nums[j]:
            j -= 1
            sr += nums[j]

        d = j - i
        if d > 1:
            return -1

        if d == 1:
            return abs(sl - sr)
        
        return min(abs(sl - sr - nums[i]), abs(sl - sr + nums[i]))

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna