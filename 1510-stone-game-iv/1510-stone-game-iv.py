class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [0] * (n + 1)
        dp[1] = 1
        for i in range(2, n + 1):
            for j in range(1, int(sqrt(i)) + 1):
                if dp[i - j * j] == 0:
                    dp[i] = 1
                    break
        return dp[n] == 1

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna