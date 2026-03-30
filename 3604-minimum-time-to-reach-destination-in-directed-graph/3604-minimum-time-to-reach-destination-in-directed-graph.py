class Solution:
    def minTime(self, n: int, edges: List[List[int]]) -> int:
        grid = defaultdict(list)
        for e in edges:
            grid[e[0]].append(e)
        heap = [(0, 0)]
        while heap:
            time, node = heapq.heappop(heap)
            if node == n - 1:
                return time
            for _, nxt, start, end in grid[node]:
                if time > end:
                    continue
                nxt_time = max(time, start) + 1
                heapq.heappush(heap, (nxt_time, nxt))
        return -1