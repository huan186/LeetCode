class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        cnt = [0] * 3
        states = {(i, 0, 0): -1 for i in range(7)}
        res = 0
        for i in range(n):
            cnt[ord(s[i])-ord('a')] += 1
            for x in [
                (0, cnt[0], cnt[1]),
                (1, cnt[0], cnt[2]),
                (2, cnt[1], cnt[2]),
                (3, cnt[0] - cnt[1], cnt[2]),
                (4, cnt[0] - cnt[2], cnt[1]),
                (5, cnt[1] - cnt[2], cnt[0]),
                (6, cnt[0] - cnt[1], cnt[0] - cnt[2]),
            ]:
                if x not in states:
                    states[x] = i
                else:
                    res = max(res, i - states[x])
        return res