class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        root = list(range(26))

        def find(x):
            if root[x] != x:
                root[x] = find(root[x])
            return root[x]

        def union(x, y):
            root[find(x)] = find(y)

        for e in equations:
            if e[1] == '=':
                union(ord(e[0]) - 97, ord(e[3]) - 97)
                
        for e in equations:
            if e[1] == '!' and find(ord(e[0]) - 97) == find(ord(e[3]) - 97):
                return False

        return True