class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        cnt = defaultdict(int)
        for i in range(n - 1):
            cnt[nums[i + 1] - nums[i]] += 1
        if cnt[1] < n - 2 and cnt[-1] < n - 2:
            return -1
        i0 = nums.index(0)
        if cnt[1]:
            return min(i0, 2 + n - i0)
        return min(i0 + 2, n - i0)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna