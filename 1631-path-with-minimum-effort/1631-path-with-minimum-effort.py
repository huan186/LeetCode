class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        inf = float('inf')
        me = [[inf] * n for _ in range(m)]
        me[0][0] = 0
        heap = [(0, 0, 0)]
        while heap:
            e, i, j = heapq.heappop(heap)
            if e > me[i][j]:
                continue
            if i == m - 1 and j == n - 1:
                return e
            for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n:
                    ne = max(e, abs(heights[i][j] - heights[ni][nj]))
                    if ne < me[ni][nj]:
                        me[ni][nj] = ne
                        heapq.heappush(heap, (ne, ni, nj))
        return -1