class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        LIMIT = 10 ** 5
        seen = defaultdict(int)
        res = 0
        for num in sorted(set(nums)):
            if num * num <= LIMIT:
                seen[num * num] = seen[num] + 1
            res = max(res, seen[num] + 1)
        return res if res > 1 else -1

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna