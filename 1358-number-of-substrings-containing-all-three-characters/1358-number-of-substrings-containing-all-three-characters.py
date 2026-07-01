class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        res = 0
        count = [0] * 3
        l = 0
        x = [ord(c) - ord('a') for c in s]
        for i in x:
            count[i] += 1
            if all(c > 0 for c in count):
                while count[x[l]] > 1:
                    count[x[l]] -= 1
                    l += 1
                res += l + 1
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna