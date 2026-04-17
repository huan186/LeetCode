class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        res = []
        for denominator in range(2, n + 1):
            for numerator in range(1, denominator):
                if numerator != 1 and gcd(denominator, numerator) != 1:
                    continue
                else:
                    res.append(str(numerator) + "/" + str(denominator))
        return res