class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        paths = [0]
        def dfs(curr):
            if curr == len(graph) - 1:
                res.append(paths[:])
                return
            for nxt in graph[curr]:
                paths.append(nxt)
                dfs(nxt)
                paths.pop()
        dfs(0)
        return res