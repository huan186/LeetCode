class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        self.ans = sum(cookies)
        counts = [0] * k
        n = len(cookies)
        def dfs(i):
            if i == n:
                self.ans = max(counts)
                return
            for j in range(k):
                if counts[j] + cookies[i] > self.ans:
                    continue
                counts[j] += cookies[i]
                dfs(i + 1)
                counts[j] -= cookies[i]
        dfs(0)
        return self.ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna