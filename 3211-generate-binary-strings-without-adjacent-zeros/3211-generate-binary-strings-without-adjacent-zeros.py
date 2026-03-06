class Solution:
    @lru_cache(None)
    def validStrings(self, n: int) -> List[str]:
        if n == 1:
            return ['0', '1']
        res = []
        ss = self.validStrings(n - 1)
        res = ['0' + s for s in ss if s[0] != '0']
        res += ['1' + s for s in ss]
        return res