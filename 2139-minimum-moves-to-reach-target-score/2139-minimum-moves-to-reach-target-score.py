class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        if target <= 2 or maxDoubles == 0:
            return target - 1
        return self.minMoves(target // 2, maxDoubles - 1) + (2 if target % 2 else 1)