class Solution:
    def smallestBalancedIndex(self, nums: list[int]) -> int:
        n = len(nums)
        inf = 10 ** 18
        postfix = [1] * n
        for i in reversed(range(n - 1)):
            postfix[i] = min(inf, postfix[i + 1] * nums[i + 1])
        total = 0
        for i in range(n):
            if total == postfix[i]:
                return i
            total += nums[i]
        return -1
        