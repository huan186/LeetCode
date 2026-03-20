class Solution:
    def __init__(self, nums: List[int]):
        self.original = nums

    def reset(self) -> List[int]:
        return self.original

    def shuffle(self) -> List[int]:
        res = self.original[:]
        for i in range(len(self.original)):
            j = random.randint(0, len(self.original)-1)
            res[i], res[j] = res[j], res[i]
        return res