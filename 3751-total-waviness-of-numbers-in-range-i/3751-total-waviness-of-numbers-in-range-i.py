class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def waviness(n):
            digits = []
            while n > 0:
                digits.append(n % 10)
                n //= 10
            w = 0
            for i in range(1, len(digits) - 1):
                if (digits[i] - digits[i - 1]) * (digits[i] - digits[i + 1]) > 0:
                    w += 1
            return w

        return sum(waviness(i) for i in range(max(101, num1), num2 + 1))

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna