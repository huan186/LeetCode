class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if s[-1] != '0':
            return False
        n = len(s)
        dp = [False] * n
        dp[0] = True
        cnt = 0

        for i in range(1, n):
            if i >= minJump and dp[i - minJump]:
                cnt += 1
            if i >= maxJump + 1 and dp[i - maxJump - 1]:
                cnt -= 1
            dp[i] = s[i] == '0' and cnt > 0

        return dp[-1]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna