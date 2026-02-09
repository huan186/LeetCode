class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        nums = []

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            nums.append(node.val)
            inorder(node.right)

        def build(l, r):
            if l > r:
                return None
            m = l + (r - l) // 2
            node = TreeNode(nums[m])
            node.left = build(l, m - 1)
            node.right = build(m + 1, r)
            return node
        
        inorder(root)
        return build(0, len(nums) - 1)