class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        res = [0] * k
        dp = [0] * k
        for num in nums:
            r = num % k
            nxt = [0] * k
            nxt[r] += 1
            for i in range(k):
                nxt[(i * r) % k] += dp[i]
            dp = nxt
            for i in range(k):
                res[i] += dp[i]
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna