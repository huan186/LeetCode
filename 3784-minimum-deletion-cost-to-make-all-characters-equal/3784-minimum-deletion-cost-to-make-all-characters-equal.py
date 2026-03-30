class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        costs = defaultdict(int)
        total_cost = 0
        for ch, c in zip(s, cost):
            costs[ch] += c
            total_cost += c
        return min(total_cost - c for c in costs.values())