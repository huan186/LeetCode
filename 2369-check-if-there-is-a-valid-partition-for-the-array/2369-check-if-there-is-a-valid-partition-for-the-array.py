class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        f0, f1, f2 = True, False, nums[0] == nums[1]

        for i in range(2, len(nums)):
            f0, f1, f2 = f1, f2, (
                f1 and nums[i] == nums[i - 1]
                or f0 and (
                    nums[i] == nums[i - 1] == nums[i - 2]
                    or nums[i] == nums[i - 1] + 1 == nums[i - 2] + 2
                )
            )

        return f2

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna