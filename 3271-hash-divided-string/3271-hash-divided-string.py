class Solution:
    def stringHash(self, s: str, k: int) -> str:
        res = []
        for i in range(0, len(s), k):
            hv = sum(ord(s[i + j]) for j in range(k)) - k * 97
            res.append(chr(hv % 26 + 97))
        return ''.join(res)