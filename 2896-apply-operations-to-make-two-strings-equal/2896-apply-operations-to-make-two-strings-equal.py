class Solution:
    def minOperations(self, s1: str, s2: str, x: int) -> int:
        pos = [i for i, (a, b) in enumerate(zip(s1, s2)) if a != b]
        m = len(pos)

        if m % 2:
            return -1
        if m == 0:
            return 0

        dp0, dp1 = 0, x

        for i in range(1, m):
            dp0, dp1 = dp1, min(
                dp1 + x,
                dp0 + 2 * (pos[i] - pos[i - 1])
            )

        return dp1 // 2

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna