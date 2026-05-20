class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        @cache
        def dfs(l, r):
            n = r - l
            if n == 1:
                return 0
            if n == 2:
                return arr[l] * arr[r - 1]
            res = inf
            for i in range(l + 1, r):
                res = min(
                    res,
                    max(arr[l:i]) * max(arr[i:r]) + dfs(l, i) + dfs(i, r)
                )
            return res
        return dfs(0, len(arr))

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna