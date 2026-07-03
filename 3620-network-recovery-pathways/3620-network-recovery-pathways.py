class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)
        max_c = 0
        graph = [[] for _ in range(n)]
        for u, v, c in edges:
            if not online[u] or not online[v] or c > k:
                continue
            graph[u].append((v, c))
            max_c = max(c, max_c)

        def valid(limit):
            h = [(0, 0)]
            dist = [float('inf')] * n
            dist[0] = 0
            while h:
                tc, cur = heapq.heappop(h)
                if tc != dist[cur]:
                    continue
                if cur == n - 1:
                    return True
                for nxt, c in graph[cur]:
                    nt = tc + c
                    if c >= limit and nt < dist[nxt] and nt <= k:
                        dist[nxt] = nt
                        heapq.heappush(h, (nt, nxt))
            return False

        res, l, r = -1, 0, max_c

        while l <= r:
            m = l + (r - l) // 2
            if valid(m):
                res = max(res, m)
                l = m + 1
            else:
                r = m - 1
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna