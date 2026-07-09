class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        a = sorted((v, i) for i, v in enumerate(nums))
        groups = [0] * n
        for i in range(1, n):
            groups[i] = groups[i - 1] + (a[i][0] - a[i - 1][0] > maxDiff)
        return [groups[l] == groups[r] for l, r in queries]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna