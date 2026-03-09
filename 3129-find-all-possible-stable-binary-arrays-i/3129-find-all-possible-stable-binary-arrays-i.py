from functools import lru_cache

class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 10**9 + 7

        @lru_cache(None)
        def dfs(z, o, last, run):
            if z == 0 and o == 0:
                return 1

            ans = 0

            # add 0
            if z > 0:
                if last == 0:
                    if run < limit:
                        ans += dfs(z-1, o, 0, run+1)
                else:
                    ans += dfs(z-1, o, 0, 1)

            # add 1
            if o > 0:
                if last == 1:
                    if run < limit:
                        ans += dfs(z, o-1, 1, run+1)
                else:
                    ans += dfs(z, o-1, 1, 1)

            return ans % MOD

        return dfs(zero, one, -1, 0)