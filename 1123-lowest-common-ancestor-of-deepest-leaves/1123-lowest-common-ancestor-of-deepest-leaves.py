class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root or not root.left and not root.right:
            return root
        def depth(node, d):
            if not node:
                return d
            return max(depth(node.left, d + 1), depth(node.right, d + 1))
        left = depth(root.left, 0)
        right = depth(root.right, 0)
        if left == right:
            return root
        if left > right:
            return self.lcaDeepestLeaves(root.left)
        return self.lcaDeepestLeaves(root.right)