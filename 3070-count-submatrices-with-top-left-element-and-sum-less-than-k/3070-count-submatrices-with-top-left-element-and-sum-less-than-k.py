class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        n = len(grid[0])
        s = [0] * (n + 1)
        res = 0
        for row in grid:
            t = [0] * (n + 1)
            for i in range(n):
                t[i + 1] += t[i] + row[i]
            for i in range(1, n + 1):
                s[i] += t[i]
                if s[i] > k:
                    break
                res += 1
        return res