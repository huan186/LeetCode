N = 5 * 10 ** 5
def linear_seive(n):
    lp = [0] * (n + 1)
    primes = []

    for i in range(2, n + 1):
        if lp[i] == 0:
            lp[i] = i
            primes.append(i)
    
        for p in primes:
            x = i * p
            if x > n or p > lp[i]:
                break
            lp[x] = p

    return primes, lp

primes, lp = linear_seive(N)

def find_good_primes():
    gp = [0]
    s = 0
    for p in primes:
        s += p
        if s > N:
            break
        if lp[s] == s:
            gp.append(s)
    return gp

gp = find_good_primes()

class Solution:
    def largestPrime(self, n: int) -> int:
        print(gp)
        return gp[bisect.bisect_right(gp, n) - 1]


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna