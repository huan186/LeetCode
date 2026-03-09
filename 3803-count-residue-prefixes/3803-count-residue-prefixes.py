class Solution:
    def residuePrefixes(self, s: str) -> int:
        res = 0
        seen = set()
        for i, c in enumerate(s):
            seen.add(c)
            if len(seen) > 2:
                break
            if (i + 1) % 3 == len(seen):
                res += 1
        return res
            