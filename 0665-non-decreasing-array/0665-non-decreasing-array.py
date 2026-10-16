class Solution:
    def checkPossibility(self, nums: list[int]) -> bool:
        n = len(nums)
        if n < 3:
            return True

        def is_ok(a, b, c):
            return a <= b <= c

        modified = False

        for i in range(1, n - 1):
            if is_ok(nums[i - 1], nums[i], nums[i + 1]):
                continue
            if modified:
                return False
            if is_ok(nums[i], nums[i], nums[i + 1]):
                nums[i - 1] = nums[i]
            elif is_ok(nums[i - 1], nums[i + 1], nums[i + 1]):
                nums[i] = nums[i + 1]
            elif is_ok(nums[i - 1], nums[i], nums[i]):
                nums[i + 1] = nums[i]
            else:
                return False
            modified = True

        return True

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna