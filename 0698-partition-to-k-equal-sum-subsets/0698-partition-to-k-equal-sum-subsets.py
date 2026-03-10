class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k:
            return False
        n = len(nums)
        target = total // k
        
        @lru_cache(None)
        def dfs(curr, used):
            if used == (1 << n) - 1:
                return True
            if curr == target:
                return dfs(0, used)
            for i in range(n):
                if not ((1 << i) & used): # bit i is free
                    if curr + nums[i] <= target and dfs(curr + nums[i], used | (1 << i)):
                        return True
            return False

        return dfs(0, 0)