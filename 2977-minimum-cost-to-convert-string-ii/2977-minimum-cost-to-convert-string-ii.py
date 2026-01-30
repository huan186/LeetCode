class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        inf = 10 ** 18

        # Floyd-Warshall
        length = set()
        v = list(set(original).union(changed))
        n = len(v)
        dist = {x: {y: 0 if x == y else inf for y in v} for x in v}
        for o, c, w in zip(original, changed, cost):
            dist[o][c] = min(dist[o][c], w)
            length.add(len(o))
            length.add(len(c))
        for k in range(n):
            for i in range(n):
                if dist[v[i]][v[k]] == inf:
                    continue
                for j in range(n):
                    if dist[v[k]][v[j]] == inf:
                        continue
                    dist[v[i]][v[j]] = min(dist[v[i]][v[j]], dist[v[i]][v[k]] + dist[v[k]][v[j]])

        # length = set(len(x) for x in v)

        # dp
        m = len(source)
        dp = [inf] * (m + 1)
        dp[0] = 0
        for i in range(m):
            if dp[i] == inf:
                continue

            if source[i] == target[i]:
                dp[i + 1] = min(dp[i + 1], dp[i])

            for l in length:
                j = i + l
                if j > m:
                    continue
                s = source[i : j]
                t = target[i : j]

                if s not in dist or t not in dist or dist[s][t] == inf:
                    continue

                dp[j] = min(dp[j], dp[i] + dist[s][t])

        return -1 if dp[-1] == inf else dp[-1]