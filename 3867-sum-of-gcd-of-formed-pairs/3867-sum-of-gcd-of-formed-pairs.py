class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        n = len(nums)
        prefixGcd = [0] * n
        mx = 0
        for i in range(n):
            mx = max(mx, nums[i])
            prefixGcd[i] = gcd(mx, nums[i])
        prefixGcd.sort()
        return sum(
            gcd(prefixGcd[i], prefixGcd[-i - 1])
            for i in range(n // 2)
        )

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna