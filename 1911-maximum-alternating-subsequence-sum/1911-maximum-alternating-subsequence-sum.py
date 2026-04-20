class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        s = 0
        i, n = 0, len(nums)
        while i < n:
            j = i
            while j + 1 < n and nums[j] > nums[j + 1]:
                j += 1
            if j != n - 1:
                s += nums[i] - nums[j]
            else:
                s += nums[i]
                break
            while j + 1 < n and nums[j + 1] >= nums[j]:
                j += 1
            i = j
        return s