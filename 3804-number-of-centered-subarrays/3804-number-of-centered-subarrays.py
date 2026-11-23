class Solution:
    def centeredSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        res = n
        for i in range(n - 1):
            s = nums[i]
            seen = set([nums[i]])
            for j in range(i + 1, n):
                s += nums[j]
                seen.add(nums[j])
                if s in seen:
                    res += 1
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna