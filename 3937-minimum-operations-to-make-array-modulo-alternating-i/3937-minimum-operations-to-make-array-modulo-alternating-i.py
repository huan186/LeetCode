class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        velmorqati = (nums, k)

        even_cost = [0] * k
        odd_cost = [0] * k

        for i, num in enumerate(nums):
            rem = num % k
            costs = even_cost if i % 2 == 0 else odd_cost

            for target in range(k):
                d = abs(rem - target)
                costs[target] += min(d, k - d)

        res = float("inf")

        for x in range(k):
            for y in range(k):
                if x != y:
                    res = min(res, even_cost[x] + odd_cost[y])

        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna