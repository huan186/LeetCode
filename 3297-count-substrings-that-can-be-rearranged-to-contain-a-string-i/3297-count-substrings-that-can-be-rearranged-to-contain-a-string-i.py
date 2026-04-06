class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        f = Counter(word2)
        res = left = 0
        missing = len(f)
        for c1 in word1:
            f[c1] -= 1
            if f[c1] == 0:
                missing -= 1
            if missing > 0:
                continue
            while f[word1[left]] < 0:
                f[word1[left]] += 1
                left += 1
            res += left + 1
        return res