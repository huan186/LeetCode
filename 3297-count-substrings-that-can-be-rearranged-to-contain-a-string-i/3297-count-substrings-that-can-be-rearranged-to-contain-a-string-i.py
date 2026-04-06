class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        freq2 = Counter(word2)
        cnt = defaultdict(int)
        left = 0
        def ok():
            for ch2, c in freq2.items():
                if c > cnt[ch2]:
                    return False
            return True
        res = 0
        for ch in word1:
            cnt[ch] += 1
            while ok():
                cnt[word1[left]] -= 1
                left += 1
                if not ok():
                    left -= 1
                    cnt[word1[left]] += 1
                    break
            if ok():
                res += left + 1
        return res