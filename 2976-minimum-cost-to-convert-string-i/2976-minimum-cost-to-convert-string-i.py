class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        if source == target:
            return 0
        graph = [[] for _ in range(26)]
        for i in range(len(original)):
            graph[ord(original[i]) - 97].append((ord(changed[i]) - 97, cost[i]))
        inf = 10 ** 9
        dist = [[inf] * 26 for _ in range(26)]
        for idx in range(26):
            heap = [(0, idx)]
            while heap:
                cost, i = heapq.heappop(heap)
                if dist[idx][i] <= cost:
                    continue
                dist[idx][i] = cost
                for j, c in graph[i]:
                    next_cost = cost + c
                    if dist[idx][j] > next_cost:
                        heapq.heappush(heap, (next_cost, j))
        min_cost = 0
        for i in range(len(source)):
            if source[i] == target[i]:
                continue
            i1, i2 = ord(source[i]) - 97, ord(target[i]) - 97
            if dist[i1][i2] == inf:
                return -1
            min_cost += dist[i1][i2]
        return min_cost