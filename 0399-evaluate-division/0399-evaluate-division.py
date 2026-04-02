class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        mapping = defaultdict(list)
        for (x, y), ratio in zip(equations, values):
            mapping[x].append((y, ratio))
            mapping[y].append((x, 1 / ratio))
        assigned = {}
        cnt = 0
        def dfs(var1):
            for var2, r in mapping[var1]:
                if var2 in assigned:
                    continue
                assigned[var2] = (assigned[var1][0] / r, cnt)
                dfs(var2)

        for (x, y), ratio in zip(equations, values):
            if x not in assigned:
                assigned[x] = (ratio, cnt)
                dfs(x)
                cnt += 1
        res = []
        for x, y in queries:
            if x not in assigned or y not in assigned or assigned[x][1] != assigned[y][1]:
                res.append(-1)
            else:
                res.append(assigned[x][0] / assigned[y][0])
        return res