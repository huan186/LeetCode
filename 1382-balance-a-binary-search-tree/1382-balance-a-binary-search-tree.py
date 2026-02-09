class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        nodes = []

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            nodes.append(node)
            inorder(node.right)

        def build(l, r):
            if l > r:
                return None
            m = (l + r) // 2
            root = nodes[m]
            root.left = build(l, m - 1)
            root.right = build(m + 1, r)
            return root

        inorder(root)
        return build(0, len(nodes) - 1)
