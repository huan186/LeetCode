class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:

        topping_costs = {0}
        def dfs(i, c):
            if i == len(toppingCosts):
                return
            dfs(i + 1, c)
            c1 = c + toppingCosts[i]
            dfs(i + 1, c1)
            topping_costs.add(c1)
            if c1 == 15:
                print(topping_costs)
            if c1 <= target:
                c2 = c1 + toppingCosts[i]
                topping_costs.add(c2)
                if c2 == 15:
                    print(topping_costs)
                dfs(i + 1, c2)
        dfs(0, 0)
        min_diff = 10 ** 18
        for bc in baseCosts:
            for tc in topping_costs:
                cost = bc + tc
                diff = cost - target
                if abs(diff) < abs(min_diff) or abs(diff) == abs(min_diff) and diff < min_diff:
                    min_diff = diff
        return target + min_diff