class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        mv = [inf] * 2
        sr = 0
        for num in nums1:
            r = num % 2
            sr += r
            mv[r] = min(mv[r], num)
        return sr == 0 or sr == len(nums1) or mv[0] > mv[1]
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna