class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n = len(source)
        parents = list(range(n))
        def find(x):
            if parents[x] != x: parents[x] = find(parents[x])
            return parents[x]
        def union(x, y): parents[find(y)] = parents[find(x)]
        for a, b in allowedSwaps: union(a, b)
        d = defaultdict(lambda: defaultdict(int))
        for i in range(n):
            p = find(i)
            d[p][source[i]] += 1
            d[p][target[i]] -= 1
        return sum(abs(f) for x in d.values() for f in x.values()) // 2