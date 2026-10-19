class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        return [i for i, x in enumerate(sorted(nums)) if x == target]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna