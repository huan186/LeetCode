class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        res = []
        for denominator in range(2, n + 1):
            for numerator in range(1, denominator):
                if gcd(denominator, numerator) == 1:
                    res.append(str(numerator) + "/" + str(denominator))
        return res