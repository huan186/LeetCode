class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)

        if n == 2 and s[0] > s[1]:
            return -1

        if list(s) == sorted(s):
            return 0

        mn = min(s)
        mx = max(s)

        if s[0] == mx and s[-1] == mn and s.count(mx) == 1 and s.count(mn) == 1:
            return 3

        if s[0] == mn or s[-1] == mx:
            return 1

        return 2

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna