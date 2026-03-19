class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        res = 0
        n = len(grid[0])
        count = [[0, 0] for _ in range(n)]
        for row in grid:
            cntX, cntY = 0, 0
            for c in range(n):
                if row[c] == 'X':
                    cntX += 1
                elif row[c] == 'Y':
                    cntY += 1
                count[c][0] += cntX
                count[c][1] += cntY
                if count[c][0] == count[c][1] and count[c][0] != 0:
                    res += 1
        return res