class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False
        cnt = 0
        for c in s:
            cnt ^= 1 << (ord(c) - 97)
        return cnt.bit_count() <= k