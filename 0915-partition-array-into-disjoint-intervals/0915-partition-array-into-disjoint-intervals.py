class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        inf = 10 ** 18
        n = len(nums)
        min_postfix = [inf] * n
        for i in range(n - 2, -1, -1):
            min_postfix[i] = min(nums[i + 1], min_postfix[i + 1])
        largest_left = 0
        for i in range(n):
            largest_left = max(largest_left, nums[i])
            if largest_left <= min_postfix[i]:
                return i + 1
        return -1