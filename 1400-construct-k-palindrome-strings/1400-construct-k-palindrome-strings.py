class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False
        return sum(v & 1 for v in Counter(s).values()) <= k