class Solution:
    def isDigitorialPermutation(self, n: int) -> bool:
        fact =[1] * 10
        for i in range(1, 10):
            fact[i] = fact[i - 1] * i
        n = str(n)
        sf = sum(fact[int(d)] for d in n)
        return Counter(n) == Counter(str(sf))

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna