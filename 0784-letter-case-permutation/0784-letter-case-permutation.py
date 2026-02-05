class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ans = ['']
        for c in s:
            if c.isalpha():
                ans = [a + c.lower() for a in ans] + [a + c.upper() for a in ans]
            else:
                ans = [a + c for a in ans]
        return ans