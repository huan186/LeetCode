class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        seen = set(nums)
        i = 1
        while True:
            if k * i not in seen:
                return k * i
            i += 1

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna