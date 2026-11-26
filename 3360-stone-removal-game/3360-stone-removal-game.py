class Solution:
    def canAliceWin(self, n: int) -> bool:
        return ((0xE1F03F807FC00 >> n) & 1) == 1

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna