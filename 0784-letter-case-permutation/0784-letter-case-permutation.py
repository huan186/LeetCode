class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        x = {''}
        for c in s:
            y = set()
            for a in x:
                    y.add(a + c.lower())
                    y.add(a + c.upper())
            x = y
        return list(x)