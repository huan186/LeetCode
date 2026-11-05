class Solution:
    def distinctPrimeFactors(self, nums: list[int]) -> int:
        primes = set()
        for num in nums:
            i = 2
            while num > 1 and i * i <= num:
                if num % i:
                    i += 1
                    continue
                primes.add(i)
                while num % i == 0:
                    num //= i
                i += 1
            if num - 1:
                primes.add(num)
        return len(primes)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna