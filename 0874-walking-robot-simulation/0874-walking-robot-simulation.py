class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obs = set(map(tuple, obstacles))
        x = y = 0
        d = 0
        dirs = [(0,1), (1,0), (0,-1), (-1,0)]
        res = 0
        for cmd in commands:
            if cmd == -2:
                d = (d - 1) % 4
            elif cmd == -1:
                d = (d + 1) % 4
            else:
                dx, dy = dirs[d]
                for _ in range(cmd):
                    nx = x + dx
                    ny = y + dy
                    if (nx, ny) in obs:
                        break
                    x, y = nx, ny
                    res = max(res, x*x + y*y)
        return res