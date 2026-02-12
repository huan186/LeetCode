class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        graph = defaultdict(set)
        for x, op, _, y in equations:
            ix = ord(x) - ord('a')
            iy = ord(y) - ord('a')
            if op == '=':
                graph[ix].add(iy)
                graph[iy].add(ix)
        visited = [-1] * 26
        def dfs(curr, v):
            visited[curr] = v
            for _next in graph[curr]:
                if visited[_next] == -1:
                    dfs(_next, v)

        cnt = 0
        for i in range(26):
            if visited[i] == -1:
                dfs(i, cnt)
                cnt += 1
                
        for x, op, _, y in equations:
            ix = ord(x) - ord('a')
            iy = ord(y) - ord('a')
            if op == '!':
                if visited[ix] == visited[iy]:
                    return False

        return True