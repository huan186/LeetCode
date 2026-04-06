class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        res = pair1 = 0
        flex = False
        for i in range((m + 1) // 2):
            for j in range((n + 1) // 2):
                pos = {(i, j), (m - i - 1, j), (i, n - j - 1), (m - i - 1, n - j - 1)}
                l = len(pos)
                if l == 1:
                    res += grid[i][j]
                else:
                    cnt1 = sum(grid[x][y] for x, y in pos)
                    res += min(cnt1, l - cnt1)
                    if l == 2:
                        if cnt1 == 1:
                            flex = True
                        elif cnt1 == 2:
                            pair1 += 2
        return res if flex or pair1 % 4 == 0 else res + 2