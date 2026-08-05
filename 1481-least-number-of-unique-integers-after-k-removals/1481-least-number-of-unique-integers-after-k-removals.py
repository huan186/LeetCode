class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        f = sorted(Counter(arr).values())
        n = len(f)
        for i in range(n):
            k -= f[i]
            if k < 0:
                return n - i
        return 0

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna