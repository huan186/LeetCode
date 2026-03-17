class Solution:
    def minCost(self, nums: List[int], x: int) -> int:
        n = len(nums)
        min_cost = nums[:]  
        res = sum(nums)

        for ops in range(1, n):
            for i in range(n):
                min_cost[i] = min(min_cost[i], nums[(i + ops) % n])
            res = min(res, sum(min_cost) + ops * x)

        return res