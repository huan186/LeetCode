class Solution:
    # def __init__(self):
    #     self.ans = None

    def minimumMoves(self, grid: List[List[int]]) -> int:
        zeros = []
        extras = []
        for i in range(3):
            for j in range(3):
                if grid[i][j] == 0:
                    zeros.append((i, j))
                else:
                    extras.append([i, j, grid[i][j] - 1])
        self.ans = math.inf
        def dfs(k, cost):
            if cost >= self.ans:
                return
            if k == len(zeros):
                self.ans = min(self.ans, cost)
                return
            zi, zj = zeros[k]
            for e in extras:
                if e[2] == 0:
                    continue
                e[2] -= 1
                dfs(k + 1, cost + abs(zi - e[0]) + abs(zj - e[1]))
                e[2] += 1
                
        dfs(0, 0)
        return self.ans