class Solution:
    def numberOfWays(self, s: str) -> int:
        rz = s.count('0')
        ro = len(s) - rz
        res = 0
        lz = lo = 0
        for c in s:
            if c == '0':
                lz += 1
                rz -= 1
                res += lo * ro
            else:
                lo += 1
                ro -= 1
                res += lz * rz
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna