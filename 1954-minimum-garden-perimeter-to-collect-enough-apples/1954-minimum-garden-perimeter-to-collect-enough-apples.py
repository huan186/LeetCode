apples = [i * (i + 1) * ((i << 1) + 1) << 1 for i in range(1 << 16)]
class Solution:
    def minimumPerimeter(self, neededApples: int) -> int:
        return bisect_left(apples, neededApples) << 3

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna