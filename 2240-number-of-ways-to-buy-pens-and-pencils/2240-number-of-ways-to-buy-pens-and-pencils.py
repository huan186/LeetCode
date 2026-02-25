class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        return sum((total - q1 * cost1) // cost2 + 1 for q1 in range(0, total // cost1 + 1))