class Solution:
    def reorganizeString(self, s: str) -> str:
        counts, n = Counter(s), len(s)
        if 2 * max(counts.values()) > n + 1:
            return ''
        res = [''] * n
        i = 0
        for c, f in sorted(counts.items(), key=lambda x: x[1], reverse=True):
            while f > 0:
                res[i] = c
                f -= 1
                i += 2
                if i >= n:
                    i = 1
        return ''.join(res)