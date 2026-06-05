# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        row = [root]
        res = []
        while row:
            res.append(-2 ** 31)
            nxt = []
            for node in row:
                res[-1] = max(res[-1], node.val)
                if node.left:
                    nxt.append(node.left)
                if node.right:
                    nxt.append(node.right)
            row = nxt
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna