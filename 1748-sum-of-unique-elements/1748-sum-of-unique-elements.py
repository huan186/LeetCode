class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        freq = Counter(nums)
        return sum(v for v in freq if freq[v] == 1)