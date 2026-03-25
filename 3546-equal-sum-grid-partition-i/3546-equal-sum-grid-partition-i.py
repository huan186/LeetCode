class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        total = sum(chain(*grid))
        def helper(x):
            return any(s * 2 == total for s in accumulate(map(sum, x)))
        return helper(grid) or helper(zip(*grid))