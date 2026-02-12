class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        in_deg = [0] * n
        out_deg = [0] * n

        def helper(node, next_node):
            if next_node != -1:
                out_deg[node] += 1
                in_deg[next_node] += 1

        for i in range(n):
            helper(i, leftChild[i])
            helper(i, rightChild[i])

        if sum(in_deg) != n - 1:
            return False

        root = -1
        for i in range(n):
            if in_deg[i] == 0:
                if root != -1:
                    return False
                root = i
            if in_deg[i] > 1 or out_deg[i] > 2:
                return False

        visited = set()

        def dfs(node):
            visited.add(node)
            if leftChild[node] != -1 and leftChild[node] not in visited:
                dfs(leftChild[node])
            if rightChild[node] != -1 and rightChild[node] not in visited:
                dfs(rightChild[node])

        dfs(root)
        return len(visited) == n