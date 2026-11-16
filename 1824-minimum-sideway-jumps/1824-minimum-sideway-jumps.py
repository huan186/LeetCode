class Solution:
    def minSideJumps(self, obstacles: list[int]) -> int:
        dp = [1, 0, 1]
        for o in obstacles[1:]:
            if o:
                dp[o - 1] = inf
            mn = min(dp)
            for i in range(3):
                if i != o - 1:
                    dp[i] = min(dp[i], mn + 1)
        return min(dp)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna