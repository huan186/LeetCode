def linear_seive(m):
    lp = [0] * (m + 1)
    primes = []

    for i in range(2, m + 1):
        if lp[i] == 0:
            lp[i] = i
            primes.append(i)
    
        for p in primes:
            x = i * p
            if x > m or p > lp[i]:
                break
            lp[x] = p

    return primes, lp

primes, lp = linear_seive(5 * 10 ** 5)

class Solution:
    def largestPrime(self, n: int) -> int:
        if n <= 1:
            return 0

        s = 0
        res = 0
        
        for p in primes:
            s += p
            if s > n:
                break
            if lp[s] == s:
                res = s
        return res


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna