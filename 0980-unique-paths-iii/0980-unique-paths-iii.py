class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        start = end = None
        obs = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    start = (i, j)
                elif grid[i][j] == 2:
                    end = (i, j)
                elif grid[i][j] == -1:
                    obs += 1
        needs = m * n - obs

        dirs = ((-1, 0), (0, 1), (1, 0), (0, -1))

        visited = {start}
        res = 0

        def dfs(x, y):
            nonlocal res
            if (x, y) == end:
                if len(visited) == needs:
                    res += 1
                return
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] != -1 and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    dfs(nx, ny)
                    visited.remove((nx, ny))

        dfs(start[0], start[1])
        return res