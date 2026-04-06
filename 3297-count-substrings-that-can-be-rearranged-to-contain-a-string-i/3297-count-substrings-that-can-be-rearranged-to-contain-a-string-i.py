class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        if len(word1) < len(word2):
            return 0
        f = Counter(word2)
        res = left = 0
        k = len(f)
        for c1 in word1:
            f[c1] -= 1
            if f[c1] == 0:
                k -= 1
            if k > 0:
                continue
            while left < len(word1) and f[word1[left]] < 0:
                f[word1[left]] += 1
                left += 1
            res += left + 1
        return res