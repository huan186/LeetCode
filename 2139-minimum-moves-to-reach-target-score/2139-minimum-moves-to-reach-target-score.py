class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        if target <= 2:
            return target - 1
        if maxDoubles == 0:
            return target - 1
        if target % 2 == 0:
            return self.minMoves(target // 2, maxDoubles - 1) + 1
        else:
            return self.minMoves(target - 1, maxDoubles) + 1