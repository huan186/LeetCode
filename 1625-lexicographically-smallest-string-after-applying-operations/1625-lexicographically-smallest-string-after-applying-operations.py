class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        n = len(s)
        res = None
        t = list(map(int, s)) * 2

        for shift in range(0, lcm(n, b), b):
            idx = n - (shift % n)

            e = 0
            min_start = 10 * t[idx] + t[idx + 1]
            for c in range(1, 100 if b % 2 else 10):
                c1, c2 = c // 10, c % 10
                d1, d2 = (t[idx] + c1 * a) % 10, (t[idx + 1] + c2 * a) % 10
                if 10 * d1 + d2 < min_start:
                    min_start = 10 * d1 + d2
                    e = c
            c1, c2 = e // 10, e % 10
            temp = t[idx: idx + n]
            for i in range(n):
                temp[i] = (temp[i] + (c2 if i % 2 else c1) * a) % 10
            if not res or temp < res:
                res = temp

        return ''.join(map(str, res))