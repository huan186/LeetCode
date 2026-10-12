class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        mod = int(1e9 + 7)
        count = [0] * 32
        for num in nums:
            for i in range(32):
                count[i] += num >> i & 1
        res = 0
        for i in range(k):
            x = sum(1 << j for j in range(32) if count[j] > i )
            if x == 0:
                break
            res = (res + x ** 2) % mod
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna