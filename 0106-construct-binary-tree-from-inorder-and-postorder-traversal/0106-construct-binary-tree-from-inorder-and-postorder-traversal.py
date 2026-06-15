# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder:
            return None
        rootVal = postorder[-1]
        rootIdx = inorder.index(rootVal)
        root = TreeNode(rootVal)
        root.left = self.buildTree(inorder[:rootIdx], postorder[:rootIdx])
        root.right = self.buildTree(inorder[rootIdx + 1:], postorder[rootIdx:-1])
        return root


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna