class Solution:
    def maxPrimes(self, n: int, s: int) -> list[int]:
        if n < 2 or s < 2:
            return []

        res = []
        lp = [0] * (n + 1)
        primes = []

        for i in range(2, n + 1):
            if not lp[i]:
                if s < i:
                    return res
                s -= i
                lp[i] = i
                primes.append(i)
                res.append(i)

            for p in primes:
                if p * i > n or p > lp[i]:
                    break
                lp[p * i] = p

        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna