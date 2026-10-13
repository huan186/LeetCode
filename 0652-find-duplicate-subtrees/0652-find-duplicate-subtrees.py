# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: TreeNode | None) -> list[TreeNode | None]:
        res = []
        seen = defaultdict(int)
        def inorder(node):
            if not node:
                return ''
            k = (str(node.val), inorder(node.left), inorder(node.right))
            if seen[k] == 1:
                res.append(node)
            seen[k] += 1
            return k
        inorder(root)
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna