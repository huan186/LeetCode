class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        n = len(nums)
        best = [0] * (n + 1)
        last = {0: 0}
        s = 0
        for i, num in enumerate(nums):
            s += num
            best[i + 1] = best[i]
            if s - target in last:
                best[i + 1] = max(best[i + 1], best[last[s - target]] + 1)
            last[s] = i + 1
        return max(best)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna