class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        left_sum, right_sum = 0, sum(nums)
        for i in range(len(nums)):
            res[i] = right_sum - left_sum - (n - 2 * i) * nums[i]
            left_sum += nums[i]
            right_sum -= nums[i]
        return res
