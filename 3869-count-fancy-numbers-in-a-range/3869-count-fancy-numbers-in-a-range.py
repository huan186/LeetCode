class Solution:
    def countFancy(self, l: int, r: int) -> int:
        def good(n):
            d = str(n)
            if len(d) == 1:
                return True
            inc = all(d[i] > d[i - 1] for i in range(1, len(d)))
            dec = all(d[i] < d[i - 1] for i in range(1, len(d)))
            return inc or dec

        good_sum = {x for x in range(136) if good(x)}

        def solve(n):
            s = str(n)

            @lru_cache(None)
            def dfs(pos, last, dir, tight, started, digit_sum): #dir = 0: undetermined, 1: inc, 2: dec, 3: invalid
                if pos == len(s):
                    if not started:
                        return 0
                    return (dir != 3) or (digit_sum in good_sum)

                limit = int(s[pos] if tight else 9)
                res = 0

                for d in range(limit + 1):
                    ntight = tight and d == limit

                    if not started:
                        if d == 0:
                            res += dfs(pos + 1, last, dir, ntight, False, digit_sum)
                        else:
                            res += dfs(pos + 1, d, 0, ntight, True, digit_sum + d)
                        continue

                    ndir = dir
                    if dir == 0:
                        if d > last:
                            ndir = 1
                        elif d < last:
                            ndir = 2
                        else:
                            ndir = 3
                    elif dir == 1:
                        if d <= last:
                            ndir = 3
                    elif dir == 2:
                        if d >= last:
                            ndir = 3

                    res += dfs(pos + 1, d, ndir, ntight, True, digit_sum + d)

                return res

            return dfs(0, 0, 0, True, False, 0)

        return solve(r) - solve(l - 1)
                
            