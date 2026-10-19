class Solution:
    def makesquare(self, matchsticks: list[int]) -> bool:
        total = sum(matchsticks)
        if total % 4:
            return False

        target = total // 4
        matchsticks.sort(reverse=True)

        if matchsticks[0] > target:
            return False

        n = len(matchsticks)

        @cache
        def dfs(used, cnt, s):
            if cnt == 3:
                return True

            if s == target:
                return dfs(used, cnt + 1, 0)

            for i, x in enumerate(matchsticks):
                if used >> i & 1 or s + x > target:
                    continue

                if dfs(used ^ 1 << i, cnt, s + x):
                    return True

            return False

        return dfs(0, 0, 0)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna