class Solution:
    def relocateMarbles(self, nums: List[int], moveFrom: List[int], moveTo: List[int]) -> List[int]:
        res = set(nums)
        for from_pos, to_pos in zip(moveFrom, moveTo):
            res.discard(from_pos)
            res.add(to_pos)
        return sorted(res)