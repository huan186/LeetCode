import heapq
from typing import List

class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        N = m * n

        # flatten index
        def idx(i, j):
            return i * n + j

        # sort cells by value
        cells = []
        for i in range(m):
            for j in range(n):
                cells.append((grid[i][j], idx(i, j)))
        cells.sort()  # increasing by value

        INF = 10**18
        dist = [[INF] * (k + 1) for _ in range(N)]

        # ptr[t]: how many cells already unlocked for teleport layer t
        ptr = [0] * (k + 1)

        pq = [(0, 0, 0)]  # (cost, used_teleport, index)
        dist[0][0] = 0

        while pq:
            cost, used, u = heapq.heappop(pq)
            if cost > dist[u][used]:
                continue

            if u == N - 1:
                return cost

            i, j = divmod(u, n)

            # normal moves
            for ni, nj in ((i + 1, j), (i, j + 1)):
                if ni < m and nj < n:
                    v = idx(ni, nj)
                    nc = cost + grid[ni][nj]
                    if nc < dist[v][used]:
                        dist[v][used] = nc
                        heapq.heappush(pq, (nc, used, v))

            # teleport
            if used < k:
                val = grid[i][j]
                p = ptr[used + 1]

                # unlock all cells with value <= val
                while p < N and cells[p][0] <= val:
                    v = cells[p][1]
                    if cost < dist[v][used + 1]:
                        dist[v][used + 1] = cost
                        heapq.heappush(pq, (cost, used + 1, v))
                    p += 1

                ptr[used + 1] = p

        return -1
