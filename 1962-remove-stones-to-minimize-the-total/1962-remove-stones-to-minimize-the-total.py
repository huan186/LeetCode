class Solution:
    def minStoneSum(self, piles: list[int], k: int) -> int:
        q = list(sorted([-p for p in piles]))
        for _ in range(k):
            heappush(q, heappop(q) // 2)
        return -sum(q)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna