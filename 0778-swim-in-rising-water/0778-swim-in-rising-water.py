class Solution:
    def swimInWater(self, grid):
        n = len(grid)
        heap = [(grid[0][0], 0, 0)]
        visited = set()
        
        while heap:
            t, x, y = heapq.heappop(heap)
            
            if (x, y) in visited:
                continue
            visited.add((x, y))
            
            if x == n - 1 and y == n - 1:
                return t
            
            for dx, dy in ((1,0), (-1,0), (0,1), (0,-1)):
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n:
                    heapq.heappush(
                        heap,
                        (max(t, grid[nx][ny]), nx, ny)
                    )