class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        # Step 1: Calculate in-degree
        in_deg = [0] * n

        for i in range(n):
            for child in (leftChild[i], rightChild[i]):
                if child != -1:
                    if in_deg[child] == 1:
                        return False
                    in_deg[child] += 1

        # Step 2: Find root
        roots = [i for i in range(n) if in_deg[i] == 0]
        if len(roots) != 1:
            return False

        root = roots[0]

        # Step 3: DFS
        visited = set()
        def dfs(node):
            if node in visited:
                return False
            visited.add(node)
            return ((leftChild[node] == -1 or dfs(leftChild[node]))
                and (rightChild[node] == -1 or dfs(rightChild[node])))

        return dfs(root) and len(visited) == n