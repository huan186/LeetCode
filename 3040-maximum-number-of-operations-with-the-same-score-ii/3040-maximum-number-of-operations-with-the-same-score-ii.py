class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        n = len(nums)
        @cache
        def dfs(i: int, j: int, target: int) -> int:
            if i >= j:
                return 0
            if i == j - 1:
                return int(nums[i] + nums[j] == target)
            ops = 0
            if nums[i] + nums[j] == target:
                ops = max(ops, 1 + dfs(i + 1, j - 1, target))
            if nums[i] + nums[i + 1] == target:
                ops = max(ops, 1 + dfs(i + 2, j, target))
            if nums[j] + nums[j - 1] == target:
                ops = max(ops, 1 + dfs(i, j - 2, target))
            return ops
        res = 0
        for s in {nums[0] + nums[1], nums[-1] + nums[-2], nums[0] + nums[-1]}:
            res = max(res, dfs(0, n - 1, s))
        return res