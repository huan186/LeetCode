# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def helper(node, parent_value):
            if not node:
                return 0
            current_value = (parent_value << 1) + node.val
            if not node.left and not node.right:
                return current_value
            return helper(node.left, current_value) + helper(node.right, current_value)
        return helper(root, 0)