class Solution:
    def numOfWays(self, n: int) -> int:
        mod = int(1e9 + 7)
        a, b = 6, 6
        for i in range(n - 1):
            a, b = (3 * a + 2 * b) % mod, (2 * a + 2 * b) % mod
        return (a + b) % mod