class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        res = []
        for l in range(max(2, len(str(low))), 10):
            for f in range(1, 11 - l):
                num = 0
                for d in range(f, f + l):
                    num = 10 * num + d
                if num > high:
                    break
                if low <= num:
                    res.append(num)
        return res


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna