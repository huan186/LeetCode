class Solution:
    def relocateMarbles(self, nums: List[int], moveFrom: List[int], moveTo: List[int]) -> List[int]:
        pos = set(nums)
        for from_pos, to_pos in zip(moveFrom, moveTo):
            pos.remove(from_pos)
            pos.add(to_pos)
        return sorted(pos)