class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factors = []
        for i in range(1, int(math.sqrt(n)) + 1):
            if i * i == n:
                factors.append(i)
            elif n % i == 0:
                factors.extend([i, n // i])
        factors.sort()
        if k > len(factors):
            return -1
        return factors[k - 1]