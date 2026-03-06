class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [-1] * n
        dp[0] = 0
        for i in range(1, n):
            for j in range(0, i):
                if dp[j] != -1 and abs(nums[j] - nums[i]) <= target:
                    dp[i] = max(dp[i], dp[j] + 1)
        return dp[-1]