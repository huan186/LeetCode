class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        prev = [set([0])] + [{x} for x in accumulate(grid[0], xor)]
        for row in grid[1:]:
            for j, x in enumerate(row):
                prev[j + 1] = {x ^ v for v in prev[j + 1] | (prev[j] if j else set())}
        return min(prev[-1])

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna