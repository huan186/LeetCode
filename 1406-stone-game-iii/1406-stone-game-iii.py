class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)

        @lru_cache(None)
        def dp(i):
            if i >= n:
                return 0
            return max(
                sum(stoneValue[i:i + j]) - dp(i + j) for j in range(1, 4)
                if i + j <= n
            )

        diff = dp(0)
        return (
            "Tie" if diff == 0 else
            "Alice" if diff > 0 else
            "Bob"
        )

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna