class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        i = 0
        for j in range((n + 1) // 2, n):
            if (nums[i] << 1) <= nums[j]:
                i += 1
        return i << 1