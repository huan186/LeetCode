class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        res = c1 = 0
        ok = False
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
                            ok = True
                        elif cnt1 == 2:
                            c1 += 2
        return res if ok or c1 % 4 == 0 else res + 2