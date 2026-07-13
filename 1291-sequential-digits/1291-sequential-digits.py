class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        lst = []
        for l in range(2, 10):
            for f in range(1, 11 - l):
                num = 0
                for d in range(f, f + l):
                    num = 10 * num + d
                lst.append(num)
        return [num for num in lst if low <= num <= high]


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna