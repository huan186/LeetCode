class Solution:
    def maximizeTheProfit(self, n: int, offers: List[List[int]]) -> int:
        endMap = defaultdict(list)
        for s, e, g in offers:
            endMap[e].append((s, g))
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = dp[i - 1]
            for s, g in endMap[i - 1]:
                dp[i] = max(dp[i], dp[s] + g)
        return dp[n]