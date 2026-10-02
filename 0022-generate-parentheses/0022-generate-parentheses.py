class Solution:
    @cache
    def generateParenthesis(self, n: int) -> list[str]:
        if n == 1:
            return ['()']

        res = set()

        for s in self.generateParenthesis(n - 1):
            for i in range(len(s) + 1):
                res.add(s[:i] + '()' + s[i:])

        return list(res)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna