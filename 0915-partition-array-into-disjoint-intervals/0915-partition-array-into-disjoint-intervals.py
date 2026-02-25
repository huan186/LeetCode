class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        n = len(nums)
        min_postfix = [0] * n
        min_postfix[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            min_postfix[i] = min(nums[i + 1], min_postfix[i + 1])
        largest_left = nums[0]
        for i in range(n):
            largest_left = max(largest_left, nums[i])
            if largest_left <= min_postfix[i]:
                return i + 1
        return -1