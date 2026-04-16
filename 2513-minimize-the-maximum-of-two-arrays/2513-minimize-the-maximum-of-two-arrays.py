class Solution:
    def minimizeSet(self, divisor1, divisor2, uniqueCnt1, uniqueCnt2):
        l = divisor1 * divisor2 // gcd(divisor1, divisor2)

        def valid(n):
            a = n // divisor1
            b = n // divisor2
            c = n // l
            only1 = b - c
            only2 = a - c
            need1 = max(0, uniqueCnt1 - only1)
            need2 = max(0, uniqueCnt2 - only2)
            both = n - a - b + c
            return both >= need1 + need2

        left, right = 1, 4 * 10**9
        while left < right:
            mid = (left + right) // 2
            if valid(mid):
                right = mid
            else:
                left = mid + 1
        return left