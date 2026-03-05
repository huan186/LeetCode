class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        prev_ord = 0
        res = 0
        for c in word:
            diff = abs(ord(c) - prev_ord)
            if diff <= 1:
                res += 1
                prev_ord = 0
            else:
                prev_ord = ord(c)
        return res