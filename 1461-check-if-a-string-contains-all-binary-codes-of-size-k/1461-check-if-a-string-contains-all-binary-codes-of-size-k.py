class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        n = 2 ** k
        if len(s) < n:
            return False
        num = 0 if k == 1 else int(s[0:k-1], 2)
        seen = set()
        for i in range(k - 1, len(s)):
           num = (num << 1) | int(s[i]) 
           seen.add(num)
           num -= int(s[i - k + 1]) << (k - 1)
        return len(seen) == n