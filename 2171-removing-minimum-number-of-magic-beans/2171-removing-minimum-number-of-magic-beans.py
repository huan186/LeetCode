class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        n = len(beans)
        if n == 1:
            return 0
        beans.sort()
        pref = [0] * n
        for i in range(1, n):
            pref[i] = pref[i - 1] + beans[i - 1]
        res = sum(beans) - beans[-1]
        cnt = 0
        for i in range(n - 2, -1, -1):
            cnt += (n - i - 1) * (beans[i + 1] - beans[i])
            res = min(res, cnt + pref[i])
        return res