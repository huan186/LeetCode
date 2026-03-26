# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        def dfs(node, depth):
            if not node.left and not node.right:
                return node, depth
            if not node.left:
                return dfs(node.right, depth + 1)
            if not node.right:
                return dfs(node.left, depth + 1)
            ln, ld = dfs(node.left, depth + 1)
            rn, rd = dfs(node.right, depth + 1)
            if ld >= rd:
                return ln, ld
            return rn, rd
        return dfs(root, 0)[0].val