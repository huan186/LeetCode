class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        target = Counter(p)
        res = []
        cnt = Counter()
        n = len(p)
        for i, c in enumerate(s):
            cnt[c] += 1
            if i >= n - 1:
                if all(target[x] == cnt[x] for x in target):
                    res.append(i - n + 1)
                cnt[s[i - n + 1]] -= 1
        return res