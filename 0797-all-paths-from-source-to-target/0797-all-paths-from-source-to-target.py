class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        visited = set()
        paths = [0]
        def dfs(curr):
            if curr == len(graph) - 1:
                res.append(paths[:])
                return
            for nxt in graph[curr]:
                if nxt not in visited:
                    visited.add(nxt)
                    paths.append(nxt)
                    dfs(nxt)
                    visited.remove(nxt)
                    paths.pop()

        dfs(0)
        return res