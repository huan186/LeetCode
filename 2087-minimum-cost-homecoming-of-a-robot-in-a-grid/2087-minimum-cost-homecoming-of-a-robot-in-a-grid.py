class Solution:
    def minCost(self, startPos: List[int], homePos: List[int], rowCosts: List[int], colCosts: List[int]) -> int:
        sr, sc = startPos
        hr, hc = homePos
        return 0 if startPos == homePos else (
            sum(rowCosts[min(sr, hr) + 1:max(sr, hr)]) +
            sum(colCosts[min(sc, hc) + 1:max(sc, hc)]) +
            (0 if sr == hr else rowCosts[hr]) +
            (0 if sc == hc else colCosts[hc])
        )