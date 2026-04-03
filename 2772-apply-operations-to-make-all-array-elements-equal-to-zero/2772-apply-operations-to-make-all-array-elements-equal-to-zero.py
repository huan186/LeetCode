class Solution:
    def checkArray(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        for i in range(n - k):
            if i + k < n:
                nums[i + k] += nums[i]
            if i > 0 and nums[i] < nums[i - 1]:
                return False
        return len(set(nums[n - k:])) == 1