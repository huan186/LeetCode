import heapq
from typing import List

class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        INF = 10**18

        # dist[i][j][t]
        dist = [[[INF] * (k + 1) for _ in range(n)] for _ in range(m)]
        dist[0][0][0] = 0

        # flatten cells sorted by value
        cells = []
        for i in range(m):
            for j in range(n):
                cells.append((grid[i][j], i, j))
        cells.sort()

        # pointer for teleport expansion per used
        ptr = [0] * (k + 1)

        pq = [(0, 0, 0, 0)]  # cost, i, j, used

        while pq:
            cost, i, j, used = heapq.heappop(pq)
            if cost > dist[i][j][used]:
                continue

            if i == m - 1 and j == n - 1:
                return cost

            # normal moves
            if j + 1 < n:
                nc = cost + grid[i][j + 1]
                if nc < dist[i][j + 1][used]:
                    dist[i][j + 1][used] = nc
                    heapq.heappush(pq, (nc, i, j + 1, used))

            if i + 1 < m:
                nc = cost + grid[i + 1][j]
                if nc < dist[i + 1][j][used]:
                    dist[i + 1][j][used] = nc
                    heapq.heappush(pq, (nc, i + 1, j, used))

            # teleport
            if used < k:
                v = grid[i][j]
                p = ptr[used]
                while p < len(cells) and cells[p][0] <= v:
                    _, x, y = cells[p]
                    if cost < dist[x][y][used + 1]:
                        dist[x][y][used + 1] = cost
                        heapq.heappush(pq, (cost, x, y, used + 1))
                    p += 1
                ptr[used] = p

        return -1
