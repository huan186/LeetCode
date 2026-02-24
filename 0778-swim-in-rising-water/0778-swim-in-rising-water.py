class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)


        visited = set()

        dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))

        def dfs(x, y, k):
            if grid[x][y] > k:
                return False
            if x == n - 1 and y == n - 1:
                return True
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    if dfs(nx, ny, k):
                        return True
            return False


        ans = 0
        left, right = 0, n * n - 1

        while left <= right:
            mid = (left + right) // 2
            visited.clear()
            if dfs(0, 0, mid):
                right = mid - 1
                ans = mid
            else:
                left = mid + 1

        return ans