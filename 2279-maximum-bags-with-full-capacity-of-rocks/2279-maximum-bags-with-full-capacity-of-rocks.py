class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        n = len(capacity)
        for i in range(n):
            rocks[i] -= capacity[i]
        rocks.sort(reverse=True)
        res = 0
        for r in rocks:
            if r >= 0:
                res += 1
            elif additionalRocks + r >= 0:
                res += 1
                additionalRocks += r
            else:
                break
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna