class Solution:
    def closestCost(self, baseCosts, toppingCosts, target):
        topping_costs = {0}
        n = len(toppingCosts)
        def dfs(i, c):
            if i == n:
                return

            dfs(i + 1, c)

            c1 = c + toppingCosts[i]
            topping_costs.add(c1)
            dfs(i + 1, c1)

            if c1 < target:
                c2 = c1 + toppingCosts[i]
                topping_costs.add(c2)
                dfs(i + 1, c2)

        dfs(0, 0)

        best = float('inf')
        for b in baseCosts:
            for t in topping_costs:
                total = b + t
                diff = total - target
                d = abs(diff) - abs(best)
                if d < 0 or d == 0 and diff < best:
                    best = diff

        return target + best
