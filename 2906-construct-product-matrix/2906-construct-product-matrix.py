class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        mod = 12345
        m, n = len(grid), len(grid[0])
        
        res = [[1] * n for _ in range(m)]
        
        pref = 1
        for i in range(m):
            for j in range(n):
                res[i][j] = pref
                pref = (pref * grid[i][j]) % mod
        
        suff = 1
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                res[i][j] = (res[i][j] * suff) % mod
                suff = (suff * grid[i][j]) % mod
        
        return res