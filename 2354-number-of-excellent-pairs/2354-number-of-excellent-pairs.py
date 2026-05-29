class Solution:
    def countExcellentPairs(self, nums: List[int], k: int) -> int:
        n = len(nums)
        m = 32
        f = [0] * m
        seen = set()
        for num in nums:
            if num in seen:
                continue
            seen.add(num)
            f[num.bit_count()] += 1
        for i in range(1, m):
            f[i] += f[i - 1]
        res = 0
        for i in range(1, m):
            c = f[i] - f[i - 1]
            if c > 0:
                need = max(1, k - i)
                if need < m:
                    res += c * (f[m - 1] - f[need - 1])
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna