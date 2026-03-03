class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        for i in range(n):
            smallest, largest = inf, -inf
            for j in range(i, n):
                smallest = min(smallest, nums[j])
                largest = max(largest, nums[j])
                res += largest - smallest
        return res