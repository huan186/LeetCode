class Solution:
    def __init__(self):
        self.p5 = [bin(p)[2:] for p in [1, 5, 25, 125, 625, 3125, 15625]]

    @lru_cache(None)
    def minimumBeautifulSubstrings(self, s: str) -> int:
        if not s:
            return 0
        min_parts = float('inf')
        for i in range(len(s)):
            if s[:i + 1] in self.p5:
                parts = self.minimumBeautifulSubstrings(s[i + 1:])
                if parts != -1:
                    min_parts = min(min_parts, 1 + parts)
        return min_parts if min_parts != float('inf') else -1