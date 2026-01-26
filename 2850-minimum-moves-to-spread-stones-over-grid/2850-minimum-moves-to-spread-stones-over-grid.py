class Solution:
    dist = None

    def __init__(self):
        if Solution.dist is None:
            Solution.dist = self.precompute()

    @staticmethod
    def precompute():
        from collections import deque
        adj = [
            (1, 3), (0, 2, 4), (1, 5),
            (0, 4, 6), (1, 3, 5, 7), (2, 4, 8),
            (3, 7), (4, 6, 8), (5, 7)
        ]
        target = sum(1 << 4 * i for i in range(9))
        q = deque([target])
        dist = {target: 0}
        while q:
            v = q.popleft()
            step = dist[v]
            for i in range(9):
                if (v >> 4 * i) & 0xF == 0x0:
                    continue
                for j in adj[i]:
                    nxt = v - (1 << 4 * i) + (1 << 4 * j)
                    if nxt not in dist:
                        dist[nxt] = step + 1
                        q.append(nxt)
        return dist

    def minimumMoves(self, grid: List[List[int]]) -> int:
        start = 0
        for r in grid:
            for x in r:
                start = (start << 4) + x
        return Solution.dist[start]