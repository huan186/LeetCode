class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        def is_prime(n):
            if n <= 1:
                return 0
            for i in range(2, int(math.sqrt(n)) + 1):
                if n % i == 0:
                    return 0
            return 1
        
        return sum(is_prime(i.bit_count()) for i in range(left, right + 1))