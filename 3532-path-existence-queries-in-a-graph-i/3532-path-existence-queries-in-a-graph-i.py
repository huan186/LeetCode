class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        groups = [0] * n
        for i in range(1, n):
            groups[i] = groups[i - 1] + (nums[i] - nums[i - 1] > maxDiff)
        return [groups[l] == groups[r] for l, r in queries]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna