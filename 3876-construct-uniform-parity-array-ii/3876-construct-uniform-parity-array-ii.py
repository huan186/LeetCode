class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        return not (reduce(or_, nums1) ^ min(nums1)) & 1
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna