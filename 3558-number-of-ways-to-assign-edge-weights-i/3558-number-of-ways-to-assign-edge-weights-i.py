class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        n = len(edges) + 1
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u - 1].append(v - 1)
            graph[v - 1].append(u - 1)
        visited = set()
        to_visit = [0]
        depth = 0
        while to_visit:
            depth += 1
            nxt_visit = []
            for curr in to_visit:
                visited.add(curr)
                for nxt in graph[curr]:
                    if nxt in visited:
                        continue
                    nxt_visit.append(nxt)
            to_visit = nxt_visit
        return pow(2, depth - 2, 10 ** 9 + 7)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna