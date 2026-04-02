class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        mapping = defaultdict(list)
        for (x, y), ratio in zip(equations, values):
            mapping[x].append((y, ratio))
            mapping[y].append((x, 1 / ratio))
        visited = {}
        assigned = {}
        cnt = 0
        def dfs(var1):
            for var2, r in mapping[var1]:
                if var2 in visited:
                    continue
                visited[var2] = cnt
                assigned[var2] = assigned[var1] / r
                dfs(var2)

        for (x, y), ratio in zip(equations, values):
            if x not in visited:
                visited[x] = cnt
                assigned[x] = ratio
                dfs(x)
                cnt += 1
        res = []
        for x, y in queries:
            if x not in assigned or y not in assigned or visited[x] != visited[y]:
                res.append(-1)
            else:
                res.append(assigned[x] / assigned[y])
        return res