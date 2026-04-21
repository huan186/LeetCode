class DSU:
    def __init__(self, n: int) -> None:
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> None:
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return
        if self.rank[rx] < self.rank[ry]:
            self.parent[rx] = ry
        elif self.rank[rx] > self.rank[ry]:
            self.parent[ry] = rx
        else:
            self.parent[ry] = rx
            self.rank[rx] += 1


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        dsu = DSU(len(s))
        for a, b in pairs:
            dsu.union(a, b)
        groups = defaultdict(list)
        characters = defaultdict(list)
        for i in range(len(s)):
            g = dsu.find(i)
            groups[g].append(i)
            characters[g].append(s[i])
        res = list(s)
        for g in groups:
            characters[g].sort()
            for i in range(len(groups[g])):
                res[groups[g][i]] = characters[g][i]
        return "".join(res)