N = 10 ** 6
lp = [0] * (N + 1)
primes = []

for i in range(2, N + 1):
    if not lp[i]:
        lp[i] = i
        primes.append(i)

    for p in primes:
        if p * i > N or p > lp[i]:
            break
        lp[p * i] = p

sp = list(accumulate(primes))

class Solution:
    def maxPrimes(self, n: int, s: int) -> list[int]:
        return primes[:min(bisect_right(primes, n), bisect_right(sp, s))]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna