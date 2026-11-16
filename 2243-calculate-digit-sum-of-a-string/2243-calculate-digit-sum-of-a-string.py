class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            tmp = []
            n = len(s)
            for i in range(0, n, k):
                tmp.append(str(sum(map(int, s[i: min(i + k, n)]))))
            s = "".join(tmp)
        return s

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna