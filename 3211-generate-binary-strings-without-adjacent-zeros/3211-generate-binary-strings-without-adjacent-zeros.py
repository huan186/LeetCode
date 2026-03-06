class Solution:
    @lru_cache(None)
    def validStrings(self, n: int) -> List[str]:
        if n == 1:
            return ['0', '1']
        ss = self.validStrings(n - 1)
        return ['0' + s for s in ss if s[0] != '0'] + ['1' + s for s in ss]