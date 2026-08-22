class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:

        def count(v):
            return sum(min(v // i, m) for i in range(1, n + 1))

        low, high = 1, m * n
        while low < high:
            mid = low + (high - low) // 2
            if count(mid) >= k:
                high = mid
            else:
                low = mid + 1

        return low

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna