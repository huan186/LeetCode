class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        def dfs(node):
            if not node:
                return 0, 0
            left = dfs(node.left)
            right = dfs(node.right)
            v = left[0] + right[0] - node.val + 1
            return v, abs(v) + left[1] + right[1]

        return dfs(root)[1]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna