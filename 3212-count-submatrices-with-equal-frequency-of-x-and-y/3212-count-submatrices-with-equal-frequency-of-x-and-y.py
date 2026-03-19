class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        res = 0
        n = len(grid[0])
        count = [[0, 0] for _ in range(n + 1)]
        for row in grid:
            temp = [[0, 0] for _ in range(n + 1)]
            for c in range(1, n +  1):
                temp[c][0], temp[c][1] = temp[c - 1][0], temp[c - 1][1]
                if row[c - 1] == 'X':
                    temp[c][0] += 1
                elif row[c - 1] == 'Y':
                    temp[c][1] += 1
            for c in range(1, n + 1):
                count[c][0] += temp[c][0]
                count[c][1] += temp[c][1]
                if count[c][0] == count[c][1] and count[c][0] != 0:
                    res += 1
        return res