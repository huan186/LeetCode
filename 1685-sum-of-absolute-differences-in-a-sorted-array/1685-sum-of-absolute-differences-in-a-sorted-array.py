class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        diff = sum(nums)
        for i in range(len(nums)):
            res[i] = diff - (n - 2 * i) * nums[i]
            diff -= nums[i] << 1
        return res
