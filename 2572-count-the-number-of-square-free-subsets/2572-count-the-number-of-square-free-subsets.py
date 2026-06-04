class Solution:
    def squareFreeSubsets(self, nums: List[int]) -> int:
        mod = 10 ** 9 + 7

        f = [0] * 31
        for num in nums:
            f[num] += 1
        arr = [(i, f[i]) for i in range(2, 31) if i % 4 and i % 9 and i % 25 and f[i]]
        n = len(arr)

        res = 0

        def dfs(i, product, ways):
            nonlocal res
            res = (res + ways) % mod
            for j in range(i, n):
                if gcd(arr[j][0], product) != 1:
                    continue
                dfs(j, product * arr[j][0], (ways * arr[j][1]) % mod)

        dfs(0, 1, 1)

        return (res * pow(2, f[1], mod) - 1) % mod

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna