class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        x = {''}
        for c in s:
            y = set()
            for a in x:
                if '1' <= c <= '9':
                    y.add(a + c)
                else:
                    y.add(a + c.lower())
                    y.add(a + c.upper())
            x = y
        return list(x)