class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        grid = defaultdict(list)
        for u, v in edges:
            grid[u].append(v)
            grid[v].append(u)
        visited = set()
        @cache
        def dfs(curr):
            visited.add(curr)
            a = b = 0
            for nxt in grid[curr]:
                if nxt not in visited:
                    na, nb = dfs(nxt)
                    a += na + 1
                    b += na + nb + 1
            return a, b
        res = [0] * n
        def cal(curr, pb):
            a, b = dfs(curr)
            if curr != 0:
                b = n + pb - 2 * a - 2
            res[curr] = b
            for nxt in grid[curr]:
                if res[nxt] == 0:
                    cal(nxt, b)
        cal(0, 0)
        return res