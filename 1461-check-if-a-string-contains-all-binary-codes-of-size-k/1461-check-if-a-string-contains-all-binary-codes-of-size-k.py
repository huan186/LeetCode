class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        need = 1 << k
        if len(s) - k + 1 < need:
            return False
        seen = set()
        mask = need - 1
        num = 0
        for i, ch in enumerate(s):
            num = ((num << 1) & mask) | (ch == '1')
            if i >= k - 1:
                seen.add(num)
                if len(seen) == need:
                    return True
        return False