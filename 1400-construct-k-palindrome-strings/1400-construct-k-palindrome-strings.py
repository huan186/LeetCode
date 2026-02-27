class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False
        return sum(1 for v in Counter(s).values() if v % 2) <= k