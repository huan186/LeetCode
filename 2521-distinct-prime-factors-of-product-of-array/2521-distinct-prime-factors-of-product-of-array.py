class Solution:
    def distinctPrimeFactors(self, nums: list[int]) -> int:
        primes = set()
        for num in nums:
            d = 2
            while d * d <= num:
                while num % d == 0:
                    primes.add(d)
                    num //= d
                d += 1
            if num - 1:
                primes.add(num)
        return len(primes)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna