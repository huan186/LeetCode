class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        res = 0
        c1 = 0
        skip = False
        for i in range((m + 1) // 2):
            for j in range((n + 1) // 2):
                pos = {(i, j), (m - i - 1, j), (i, n - j - 1), (m - i - 1, n - j - 1)}
                l = len(pos)
                if l == 1:
                    res += grid[i][j]
                else:
                    cnt1 = 0
                    for (x, y) in pos:
                        cnt1 += grid[x][y]
                    if l == 2 :
                        if cnt1 == 1:
                            skip = True
                        elif cnt1 == 2:
                            c1 += 2
                    res += min(cnt1, l - cnt1)
        return res if skip or c1 % 4 == 0 else res + 2