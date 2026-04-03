class Solution:
    def maxWalls(self, robots: List[int], distance: List[int], walls: List[int]) -> int:
        z = sorted(zip(robots, distance))
        walls.sort()
        left, right, ri = 0, 0, 0
        for i, (robot, dist) in enumerate(z):
            prev_robot = 0 if i == 0 else z[i - 1][0]
            next_robot = 10 ** 18 if i == len(z) - 1 else z[i + 1][0]
            l = bisect.bisect_left(walls, max(prev_robot + 1, robot - dist))
            ml = bisect.bisect_right(walls, robot)
            mr = bisect.bisect_left(walls, robot)
            r = bisect.bisect_right(walls, min(next_robot - 1, robot + dist))
            left, right = max(left + ml - l, right + ml - max(l, ri)), max(left, right) + r - mr
            ri = r
        return max(left, right)