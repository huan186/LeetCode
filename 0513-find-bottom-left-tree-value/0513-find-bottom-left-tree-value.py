# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        def dfs(node, depth):
            if not node:
                return depth - 1, node
            if not node.left and not node.right:
                return depth, node
            left = dfs(node.left, depth + 1)
            right = dfs(node.right, depth + 1)
            if left[0] >= right[0]:
                return left
            return right
        return dfs(root, 0)[1].val