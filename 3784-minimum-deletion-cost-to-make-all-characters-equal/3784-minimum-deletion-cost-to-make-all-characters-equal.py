class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        costs = defaultdict(int)
        for ch, c in zip(s, cost):
            costs[ch] += c
        return sum(cost) - max(costs.values())