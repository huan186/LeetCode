class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        def sum_of_digits(x):
            return sum(map(int, str(x)))
        l = len(str(n))
        x = 10 ** l - n
        for i in range(l + 1):
            r = x % 10 ** i
            print(r)
            if sum_of_digits(n + r) <= target:
                return r
        return -1

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna