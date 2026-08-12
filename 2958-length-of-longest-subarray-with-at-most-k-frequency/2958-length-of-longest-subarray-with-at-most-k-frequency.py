class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        left = 0
        res = 0
        f = defaultdict(int)
        for right in range(len(nums)):
            f[nums[right]] += 1
            while f[nums[right]] > k:
                f[nums[left]] -= 1
                left += 1
            res = max(res, right - left + 1)
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna