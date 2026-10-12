class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        mod = int(1e9 + 7)
        count = [0] * 32
        for num in nums:
            for i in range(32):
                count[i] += (num >> i) & 1
                # num >>= 1
        res = 0
        for i in range(k):
            x = 0
            for i in range(32):
                if count[i] == 0:
                    continue
                x |= 1 << i
                count[i] -= 1
            res = (res + x * x) % mod
        return res
            

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna