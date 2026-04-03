class Solution:
    def checkArray(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        for i in range(n - 1):
            if i > 0 and nums[i] < nums[i - 1]:
                return False
            if i + k < n:
                nums[i + k] += nums[i]
            elif nums[i] != nums[i + 1]:
                return False
        return True