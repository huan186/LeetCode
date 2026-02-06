class Solution:
    def stringHash(self, s: str, k: int) -> str:
        res = []
        for i in range(0, len(s), k):
            hv = 0
            for j in range(k):
                hv += ord(s[i + j]) - ord('a')
            res.append(chr(hv % 26 + ord('a')))
        return ''.join(res)