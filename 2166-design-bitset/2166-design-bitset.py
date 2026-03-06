class Bitset:

    def __init__(self, size: int):
        self.size = size
        self.flipped = False
        self.ones = set()

    def fix(self, idx: int) -> None:
        if not self.flipped:
            self.ones.add(idx)
        else:
            self.ones.discard(idx)

    def unfix(self, idx: int) -> None:
        if not self.flipped:
            self.ones.discard(idx)
        else:
            self.ones.add(idx)

    def flip(self) -> None:
        self.flipped = not self.flipped

    def all(self) -> bool:
        return self.count() == self.size

    def one(self) -> bool:
        return self.count() > 0

    def count(self) -> int:
        return self.size - len(self.ones) if self.flipped else len(self.ones)

    def toString(self) -> str:
        res = []
        for i in range(self.size):
            v = 1 if i in self.ones else 0
            if self.flipped:
                v = 1 - v
            res.append(str(v))
        return ''.join(res)