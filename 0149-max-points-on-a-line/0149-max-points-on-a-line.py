class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        
        if n <= 2:
            return n

        def gcd(a, b):
            return a if b == 0 else gcd(b, a % b)

        res = 0
        inf = float('inf')

        def cal_slope(i1, i2):
            x1, y1 = points[i1]
            x2, y2 = points[i2]
            dx = x1 - x2
            dy = y1 - y2
            if dx == 0:
                return (inf, inf)
            l = gcd(dx, dy)
            dx //= l
            dy //= l
            if dx < 0:
                dx = -dx
                dy = -dy
            return (dx, dy)

        for i in range(n - 1):
            slopes = {}
            for j in range(i + 1, n):
                slope = cal_slope(i, j)
                slopes[slope] = slopes.get(slope, 1) + 1
                res = max(res, slopes[slope])

        return res