class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        @lru_cache(None)
        def dp(l, r):
            if l == r:
                return piles[l]
            return max(piles[l] - dp(l + 1, r), piles[r] - dp(l, r - 1))
        return dp(0, len(piles) - 1) > 0

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna