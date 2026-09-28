class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        dp = 0
        best = -prices[0]
        for i in range(1, len(prices)):
            dp, best = max(dp, prices[i] - fee + best), max(best, dp - prices[i])
        return dp

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna