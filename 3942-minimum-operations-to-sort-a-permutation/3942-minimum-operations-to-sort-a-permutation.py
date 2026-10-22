class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0

        inc = all(nums[(i + 1) % n] == (nums[i] + 1) % n
                  for i in range(n))
        dec = all(nums[(i + 1) % n] == (nums[i] - 1) % n
                  for i in range(n))

        if not inc and not dec:
            return -1

        i = nums.index(0)
        return min(i, n - i + 2) if inc else min(i + 2, n - i)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna