class Solution:
    def isThree(self, n: int) -> bool:
        def is_prime(x):
            if x < 2:
                return False
            for i in range(2, int(math.sqrt(x)) + 1):
                if x % i == 0:
                    return False
            return True
        sqrt = int(math.sqrt(n))
        return is_prime(sqrt) and sqrt ** 2 == n