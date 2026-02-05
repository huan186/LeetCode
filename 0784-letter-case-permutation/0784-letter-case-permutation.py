class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ans = {''}
        for c in s:
            temp = set()
            for a in ans:
                    temp.add(a + c.lower())
                    temp.add(a + c.upper())
            ans = temp
        return list(ans)