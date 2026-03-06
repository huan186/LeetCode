class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        def sqr_distance(x1, y1, x2, y2):
            return (x1 - x2) ** 2 + (y1 - y2) ** 2

        points = set()
        for x, y, r in circles:
            sqr_r = r ** 2
            for i in range(x - r, x + r + 1):
                for j in range(y - r, y + r + 1):
                    if (i, j) not in points and sqr_distance(x, y, i, j) <= sqr_r:
                        points.add((i, j))

        return len(points)