class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        cost = min(need1, need2) * min(cost1 + cost2, costBoth)
        if need1 >= need2:
            cost += (need1 - need2) * min(cost1, costBoth)
        else:
            cost += (need2 - need1) * min(cost2, costBoth)
        return cost

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna