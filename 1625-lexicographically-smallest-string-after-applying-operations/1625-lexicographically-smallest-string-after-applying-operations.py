class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        n = len(s)
        best = None
        digits = list(map(int, s)) * 2
        best_pref = 99
        for shift in range(0, lcm(n, b), b):
            start_idx = n - (shift % n)

            best_c0, best_c1 = 0, 0
            d0, d1 = digits[start_idx], digits[start_idx + 1]
            min_pref = 10 * d0 + d1
            for c0 in range(10 if b % 2 else 1):
                for c1 in range(10):
                    pref = 10 * ((d0 + c0 * a) % 10) + (d1 + c1 * a) % 10
                    if pref < min_pref:
                        min_pref = pref
                        best_c0, best_c1 = c0, c1
            if min_pref > best_pref:
                continue
            best_pref = min_pref

            t = digits[start_idx: start_idx + n]
            for i in range(n):
                t[i] = (t[i] + (best_c1 if i % 2 else best_c0) * a) % 10
            if not best or t < best:
                best = t

        return ''.join(map(str, best))