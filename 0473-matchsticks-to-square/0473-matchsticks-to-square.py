class Solution:
    def makesquare(self, matchsticks: list[int]) -> bool:
        total = sum(matchsticks)
        target = total // 4
        if total % 4:
            return False
        matchsticks.sort()
        if matchsticks[-1] > target:
            return False
        n = len(matchsticks)

        @cache
        def dfs(used, cnt, s):
            if s == target:
                cnt += 1
                s = 0
            if cnt == 3:
                return True
            for i in range(n):
                if used >> i & 1:
                    continue
                if s + matchsticks[i] > target:
                    return False
                if dfs(used ^ 1 << i, cnt, s + matchsticks[i]):
                   return True
            return False

        return dfs(0, 0, 0)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna