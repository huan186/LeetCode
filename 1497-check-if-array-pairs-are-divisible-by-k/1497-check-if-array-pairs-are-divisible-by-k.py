class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        f = Counter()
        for num in arr:
            f[num % k] += 1
        return f[0] % 2 == 0 and all(f[i] == f[k - i] for i in range(1, k // 2 + 1))


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna