class Solution:
    def minCost(self, nums: List[int], x: int) -> int:
        n = len(nums)
        dp = nums[:]  
        res = sum(nums)

        for ops in range(1, n):
            for i in range(n):
                dp[i] = min(dp[i], nums[(i + ops) % n])
            res = min(res, sum(dp) + ops * x)

        return res