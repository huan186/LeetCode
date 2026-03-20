class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        res = [[0] * (n - k + 1) for _ in range(m - k + 1)]
        for i in range(m - k + 1):
            for j in range(n - k + 1):
                s = set()
                for di in range(0, k):
                    for dj in range(0, k):
                        s.add(grid[i + di][j + dj])
                if len(s) == 1:
                    continue
                l = sorted(list(s))
                res[i][j] = min(a - b for a, b in zip(l[1:], l))
        return res