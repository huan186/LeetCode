class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)

        q = deque()
        def dfs(i, j):
            q.append((i, j))
            grid[i][j] = -1
            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] == 1:
                    dfs(ni, nj)

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i, j)
                    break
            else:
                continue
            break
        while q:
            i, j = q.popleft()
            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < n and 0 <= nj < n:
                    if grid[ni][nj] == 1:
                        return -grid[i][j] - 1
                    elif grid[ni][nj] == 0:
                        grid[ni][nj] = grid[i][j] - 1
                        q.append((ni, nj))
        return 0