class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] != 0 or grid[-1][-1] != 0:
            return -1
        m, n = len(grid), len(grid[0])
        queue = deque([(1, 0, 0)])
        visited = [[False] * n for _ in range(m)]
        visited[0][0] = True
        while queue:
            cost, x, y = queue.popleft()
            if x == m - 1 and y == n - 1:
                return cost
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if dx == dy == 0:
                        continue
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and grid[nx][ny] == 0:
                        queue.append((cost + 1, nx, ny))
                        visited[nx][ny] = True
        return -1