class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        n = len(nums)
        for i in range(n):
            nums[i] %= k
        res = inf
        for x in range(k):
            for y in range(k):
                if x == y:
                    continue
                ops = 0
                for i, num in enumerate(nums):
                    target = x if i % 2 == 0 else y
                    d = abs(num - target)
                    ops += min(d, k - d)
                res = min(res, ops)
        return res
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna