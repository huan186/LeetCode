class Solution:
    def minimumCost(self, source, target, original, changed, cost):
        graph = [{} for _ in range(26)]
        for o, c, w in zip(original, changed, cost):
            i1, i2 = ord(o) - 97, ord(c) - 97
            if i2 in graph[i1]:
                graph[i1][i2] = min(graph[i1][i2], w)
            else:
                graph[i1][i2] = w
        inf = 10 ** 18
        dist = [[inf] * 26 for _ in range(26)]
        for s in range(26):
            heap = [(0, s)]
            while heap:
                cur_cost, u = heapq.heappop(heap)
                if dist[s][u] <= cur_cost:
                    continue
                dist[s][u] = cur_cost
                for v, w in graph[u].items():
                    if cur_cost + w < dist[s][v]:
                        heapq.heappush(heap, (cur_cost + w, v))
        ans = 0
        for a, b in zip(source, target):
            u, v = ord(a) - 97, ord(b) - 97
            if dist[u][v] == inf:
                return -1
            ans += dist[u][v]
        return ans