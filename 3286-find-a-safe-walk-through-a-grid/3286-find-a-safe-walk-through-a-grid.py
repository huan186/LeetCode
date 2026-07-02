class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])
        start_health = health - grid[0][0]
        if start_health == 0:
            return False
        dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))
        mh = [(-start_health, 0, 0)]
        while mh:
            h, x, y = heapq.heappop(mh)
            h = -h
            if grid[x][y] == 2:
                continue
            grid[x][y] = 2
            if x == m - 1 and y == n - 1:
                return True
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and h - grid[nx][ny] > 0:
                    heapq.heappush(mh, (-h + grid[nx][ny], nx, ny))
        return False

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna