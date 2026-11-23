class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: list[list[int]]) -> int:
        n = len(stations)
        dp = [startFuel] * (n + 1)

        for i, (pos, fuel) in enumerate(stations):
            for j in range(i, -1, -1):
                if dp[j] >= pos:
                    dp[j + 1] = max(dp[j + 1], dp[j] + fuel)
        
        return next((i for i, dist in enumerate(dp) if dist >= target), -1)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna