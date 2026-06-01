class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)
        j = min_cost = 0
        for i in range(len(cost)):
            j += 1
            if j % 3 == 0:
                continue
            min_cost += cost[i]
        return min_cost

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna