class Solution:
    @cache
    def diffWaysToCompute(self, expr: str) -> List[int]:
        res = []
        for i, c in enumerate(expr):
            if c in "+-*":
                left = self.diffWaysToCompute(expr[:i])
                right = self.diffWaysToCompute(expr[i+1:])

                for l in left:
                    for r in right:
                        if c == '+':
                            res.append(l + r)
                        elif c == '-':
                            res.append(l - r)
                        else:
                            res.append(l * r)
        return res if res else [int(expr)]
