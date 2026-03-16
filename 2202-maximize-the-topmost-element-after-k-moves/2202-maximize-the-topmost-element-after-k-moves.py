class Solution:
    def maximumTop(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if n == 1:
            if k % 2 == 0:
                return nums[0]
            return -1
        if k <= 1:
            return nums[k]
        if k < n:
            return max(max(nums[: k - 1]), nums[k])
        if k == n:
            return max(nums[:-1])
        return max(nums)