# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        def dfs(node):
            if not node:
                return 0, 0, 0 # cnt, sum, valid
            lc, ls, lv = dfs(node.left)
            rc, rs, rv = dfs(node.right)
            cc = lc + rc + 1
            cs = ls + rs + node.val
            cv = lv + rv + (cs // cc == node.val)
            return cc, cs, cv
        
        return dfs(root)[2]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna