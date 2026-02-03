class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        j, n = 0, len(nums)
        while j < n - 2 and nums[j] < nums[j + 1]:
            j += 1
        if j == 0:
            return False
        i = j
        while j < n - 2 and nums[j] > nums[j + 1]:
            j += 1
        if j == i:
            return False
        while j < n - 1 and nums[j] < nums[j + 1]:
            j += 1
        return j == n - 1