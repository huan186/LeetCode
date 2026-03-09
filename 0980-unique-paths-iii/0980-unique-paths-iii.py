class Solution:
    def uniquePathsIII(self, grid):
        m, n = len(grid), len(grid[0])
        empty = 1
        sx = sy = ex = ey = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    empty += 1
                elif grid[i][j] == 1:
                    sx, sy = i, j
                elif grid[i][j] == 2:
                    ex, ey = i, j

        def dfs(x, y, remain):
            if (x, y) == (ex, ey):
                return remain == 0

            tmp = grid[x][y]
            grid[x][y] = -1
            paths = 0

            for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] >= 0:
                    paths += dfs(nx, ny, remain - 1)

            grid[x][y] = tmp
            return paths

        return dfs(sx, sy, empty)