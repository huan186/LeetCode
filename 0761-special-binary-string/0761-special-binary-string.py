class Solution:
    @lru_cache(None)
    def makeLargestSpecial(self, s: str) -> str:
        i, n = 0, len(s)
        parts = []
        while i < n:
            d = 1
            j = i + 1
            while j < n and d > 0:
                d += 1 if s[j] == '1' else -1
                j += 1
            parts.append('1' + self.makeLargestSpecial(s[i + 1 : j - 1]) + '0')
            i = j
        parts.sort(reverse=True)
        return ''.join(parts)
                