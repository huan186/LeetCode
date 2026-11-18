class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        cnt = defaultdict(int)
        for r in responses:
            for x in set(r):
                cnt[x] += 1
        m = max(cnt.values())
        res = ''
        for k, v in cnt.items():
            if v == m and (not res or res > k):
                res = k
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna