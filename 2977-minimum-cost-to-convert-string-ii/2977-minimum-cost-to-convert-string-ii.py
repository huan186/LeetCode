from collections import defaultdict
from typing import List


class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        inf = 10 ** 18

        # Floyd-Warshall
        v = list(set(original).union(changed))
        n = len(v)
        dist = {x: {y: 0 if x == y else inf for y in v} for x in v}
        for o, c, w in zip(original, changed, cost):
            dist[o][c] = min(dist[o][c], w)
        for k in range(n):
            for i in range(n):
                if dist[v[i]][v[k]] == inf:
                    continue
                for j in range(n):
                    if dist[v[k]][v[j]] == inf:
                        continue
                    dist[v[i]][v[j]] = min(dist[v[i]][v[j]], dist[v[i]][v[k]] + dist[v[k]][v[j]])

        # group by length
        by_length = defaultdict(list)
        for x in v:
            by_length[len(x)].append(x)

        # dp
        m = len(source)
        dp = [inf] * (m + 1)
        dp[0] = 0
        for i in range(m):
            if dp[i] == inf:
                continue
            
            if source[i] == target[i]:
                dp[i + 1] = min(dp[i + 1], dp[i])
            
            for length in by_length:
                j = i + length
                if j > m:
                    continue
                s = source[i : j]
                t = target[i : j]
                
                if s not in dist or t not in dist:
                    continue

                if c != inf:
                    dp[j] = min(dp[j], dp[i] + dist[s][t])
        
        return -1 if dp[-1] == inf else dp[-1]
        