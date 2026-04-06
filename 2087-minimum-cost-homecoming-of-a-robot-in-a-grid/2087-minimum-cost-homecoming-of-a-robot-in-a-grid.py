class Solution:
    def minCost(self, startPos: List[int], homePos: List[int], rowCosts: List[int], colCosts: List[int]) -> int:
        dx = -1 if startPos[0] > homePos[0] else 1
        dy = -1 if startPos[1] > homePos[1] else 1
        return (sum(rowCosts[x] for x in range(startPos[0] + dx, homePos[0] + dx, dx)) +
                sum(colCosts[y] for y in range(startPos[1] + dy, homePos[1] + dy, dy)))