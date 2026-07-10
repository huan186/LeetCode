class Solution:
    def numberOfGoodSubarraySplits(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7
        prev = -1
        res = 1

        for i, x in enumerate(nums):
            if x:
                if prev != -1:
                    res = res * (i - prev) % MOD
                prev = i

        return res if prev != -1 else 0

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna