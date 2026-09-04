class Solution:
    def compareBitonicSums(self, nums: list[int]) -> int:
        asc = 0
        i, n = 0, len(nums)
        while i < n and nums[i] < nums[i + 1]:
            asc += nums[i]
            i += 1
        diff = 2 * asc + nums[i] - sum(nums)
        print(diff)
        return -1 if diff == 0 else (0 if diff > 0 else 1)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna