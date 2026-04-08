class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)

        def dfs(i, j, l):
            l.append((i, j))
            grid[i][j] = 0
            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] == 1:
                    dfs(ni, nj, l)
        l1, l2 = [], []
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    if not l1:
                        dfs(i, j, l1)
                    else:
                        dfs(i, j, l2)
        min_flips = 2 * n
        for i1, j1 in l1:
            for i2, j2 in l2:
                min_flips = min(min_flips, abs(i1 - i2) + abs(j1 - j2) - 1)
        return min_flips