class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        res = None
        max_depth = -1
        def dfs(node, d):
            nonlocal res, max_depth
            if not node:
                max_depth = max(d, max_depth)
                return d
            l = dfs(node.left, d + 1)
            r = dfs(node.right, d + 1)
            if l == r == max_depth:
                res = node
            return max(l, r)
        dfs(root, 0)
        return res