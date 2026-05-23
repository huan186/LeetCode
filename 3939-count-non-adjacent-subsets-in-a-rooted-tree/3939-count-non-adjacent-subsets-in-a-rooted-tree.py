class Solution:
    def countValidSubsets(self, parent: List[int], nums: List[int], k: int) -> int:
        mod = 10 ** 9 + 7
        n = len(parent)
        children = [[] for _ in range(n)]
        for i in range(1, n):
            children[parent[i]].append(i)

        dp0 = [[0] * k for _ in range(n)]
        dp1 = [[0] * k for _ in range(n)]

        def merge(a, b):
            res = [0] * k
            for i in range(k):
                if a[i] == 0:
                    continue
                for j in range(k):
                    if b[j] == 0:
                        continue
                    res[(i + j) % k] = (res[(i + j) % k] + a[i] * b[j]) % mod 
            return res

        for u in range(n - 1, - 1, -1):
            dp0[u][0] = 1
            dp1[u][nums[u] % k] = 1

            for v in children[u]:
                child_total = [(dp0[v][r] + dp1[v][r]) % mod for r in range(k)]
                dp0[u] = merge(dp0[u], child_total)
                dp1[u] = merge(dp1[u], dp0[v])

        total = (dp0[0][0] + dp1[0][0]) % mod
        return (total - 1) % mod

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna