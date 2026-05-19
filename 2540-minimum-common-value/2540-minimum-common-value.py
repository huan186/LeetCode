class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        i = j = 0
        n, m = len(nums1), len(nums2)
        while i < n and j < m:
            diff = nums1[i] - nums2[j]
            if diff == 0:
                return nums1[i]
            if diff > 0:
                j += 1
            else:
                i += 1
        return -1

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna