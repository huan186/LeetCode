class Solution:
    def minArraySum(self, nums: list[int]) -> int:
        freq = Counter(nums)
        ans = 0
        largest = max(freq)

        for x in sorted(freq):
            cnt = freq[x]
            if not cnt:
                continue
            for y in range(x * 2, largest + 1, x):
                cnt += freq[y]
                freq[y] = 0
            ans += cnt * x

        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna