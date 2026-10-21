class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        MOD = 10**9 + 7
        if p == 1:
            return 1

        return (pow(2, p, MOD) - 1) * pow(
            pow(2, p, MOD) - 2,
            pow(2, p - 1) - 1,
            MOD
        ) % MOD

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna