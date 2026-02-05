class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        words = set(wordDict)
        dp = [True] + [False] * n
        for i in range(1, n + 1):
            for j in range(i):
                dp[i] |= dp[j] and s[j : i] in words
        return dp[n]