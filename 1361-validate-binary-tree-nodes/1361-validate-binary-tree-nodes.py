class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        in_deg = [0] * n
        parents = list(range(n))

        def find(x):
            if parents[x] != x:
                parents[x] = find(parents[x])
            return parents[x]

        def union(x, y):
            rx, ry = find(x), find(y)
            if rx == ry:
                return False
            parents[ry] = rx
            return True

        components = n
        for i in range(n):
            for child in (leftChild[i], rightChild[i]):
                if child == -1:
                    continue
                if in_deg[child] == 1 or not union(i, child):
                    return False
                in_deg[child] += 1
                components -= 1
                
        return components == 1