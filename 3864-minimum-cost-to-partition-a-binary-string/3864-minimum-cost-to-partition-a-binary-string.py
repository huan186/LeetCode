class Solution:
    def minCost(self, s: str, encCost: int, flatCost: int) -> int:
        n = len(s)

        pref = [0]*(n+1)
        for i in range(n):
            pref[i+1] = pref[i] + (s[i] == '1')

        def dfs(l, r):
            L = r - l + 1
            X = pref[r+1] - pref[l]

            if X == 0:
                base = flatCost
            else:
                base = L * X * encCost

            if L % 2 == 1:
                return base

            mid = (l+r)//2
            return min(base, dfs(l, mid) + dfs(mid+1, r))

        return dfs(0, n-1)