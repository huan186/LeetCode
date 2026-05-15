class Solution:
    def isDigitorialPermutation(self, n: int) -> bool:
        fact = [1] * 10
        for i in range(1, 10):
            fact[i] = fact[i - 1] * i
        freq = [0] * 10
        sf = 0
        while n:
            d = n % 10
            sf += fact[d]
            freq[d] += 1
            n //= 10
        while sf:
            freq[sf % 10] -= 1
            sf //= 10
        return not any(freq)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna