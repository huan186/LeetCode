class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        s = '123456789'
        res = []
        for l in range(len(str(low)), len(str(high)) + 1):
            for i in range(10 - l):
                num = int(s[i : i + l])
                if low <= num <= high:
                    res.append(num)
        return res


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna