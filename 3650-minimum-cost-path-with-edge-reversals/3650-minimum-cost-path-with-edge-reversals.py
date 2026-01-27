class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for u, v, cost in edges:
            graph[u].append((v, cost))
            graph[v].append((u, 2 * cost))
        inf = 10 ** 9
        min_cost = [inf] * n
        heap = [(0, 0)]
        while heap:
            total_cost, node = heapq.heappop(heap)
            if min_cost[node] <= total_cost:
                continue
            min_cost[node] = total_cost
            for next_node, cost in graph[node]:
                if total_cost + cost < min_cost[next_node]:
                    heapq.heappush(heap, (total_cost + cost, next_node))
        return -1 if min_cost[-1] == inf else min_cost[-1]