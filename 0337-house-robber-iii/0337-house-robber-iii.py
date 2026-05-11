class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0, 0

            lt, ls = dfs(node.left)
            rt, rs = dfs(node.right)

            take = node.val + ls + rs
            skip = max(lt, ls) + max(rt, rs)

            return take, skip

        return max(dfs(root))

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna