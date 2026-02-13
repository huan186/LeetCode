class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        cnt = [0] * 3
        states = {}
        for i in range(7):
            states[(i, 0, 0)] = -1
        res = 0
        for i in range(n):
            cnt[ord(s[i])-ord('a')] += 1
            for x in [
                (1, cnt[0], cnt[1]),
                (2, cnt[0], cnt[2]),
                (3, cnt[1], cnt[2]),
                (4, cnt[0] - cnt[1], cnt[2]),
                (5, cnt[0] - cnt[2], cnt[1]),
                (6, cnt[1] - cnt[2], cnt[0]),
                (7, cnt[0] - cnt[1], cnt[0] - cnt[2]),
            ]:
                if x not in states:
                    states[x] = i
                else:
                    res = max(res, i - states[x])
        return res