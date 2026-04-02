class Solution:
    def minRemovals(self, nums: List[int], target: int) -> int:
        dp = {0: 0}
        for num in nums:
            target ^= num
            for v, c in list(dp.items()):
                if c + 1 < dp.get(v ^ num, inf):
                    dp[v ^ num] = c + 1
        return dp.get(target, -1)
