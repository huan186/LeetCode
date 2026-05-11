class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        return list(map(int, "".join(map(str, nums))))