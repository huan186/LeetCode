class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = [[0, chr(97 + i)] for i in range(26)]
        for c in s:
            freq[ord(c) - ord('a')][0] += 1
        freq.sort(reverse=True)
        f_max = freq[0][0]
        n = len(s)
        if 2 * f_max > n + 1:
            return ''
        res = [''] * n
        i = 0
        for f, c in freq:
            if f == 0:
                break
            while f > 0:
                res[i] = c
                i += 2
                if i >= n:
                    i = 1
                f -= 1
        return ''.join(res)