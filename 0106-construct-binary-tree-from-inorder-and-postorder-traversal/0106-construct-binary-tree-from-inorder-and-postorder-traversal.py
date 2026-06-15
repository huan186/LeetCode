# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        inorder_indices = {v: i for i, v in enumerate(inorder)}

        def build_tree(l1, r1, l2, r2):
            if l1 > r1:
                return None
            val = postorder[r2]
            idx = inorder_indices[val]
            left_size = idx - l1
            node = TreeNode(val)
            node.left = build_tree(l1, idx - 1, l2, l2 + left_size - 1)
            node.right = build_tree(idx + 1, r1, l2 + left_size, r2 - 1)
            return node

        return build_tree(0, len(inorder) - 1, 0, len(postorder) - 1)


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna