class Robot:

    def __init__(self, width: int, height: int):
        self.w = width
        self.h = height
        self.perimeter = 2 * (width + height) - 4
        self.x = [
            self.w - 1,
            self.w - 1 + self.h - 1,
            self.w - 1 + self.h - 1 + self.w - 1,
            self.perimeter
        ]
        self.pos = 0
        self.moved = False

    def step(self, num: int) -> None:
        self.pos = (self.pos + num) % self.perimeter
        self.moved = True

    def getPos(self) -> List[int]:
        pos = self.pos
        if pos <= self.x[0]:
            return [pos, 0]
        if pos <= self.x[1]:
            return [self.w - 1, pos - self.x[0]]
        if pos <= self.x[2]:
            return [self.w - 1 - (pos - self.x[1]), self.h - 1]
        return [0, self.h - 1 - (pos - self.x[2])]

    def getDir(self) -> str:
        pos = self.pos
        if self.pos == 0 and self.moved:
            return "South"
        if pos <= self.x[0]:
            return "East"
        if pos <= self.x[1]:
            return "North"
        if pos <= self.x[2]:
            return "West"
        return "South"