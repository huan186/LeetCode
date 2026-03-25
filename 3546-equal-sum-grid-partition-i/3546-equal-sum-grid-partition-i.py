class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        total = sum(chain(*grid))
        def helper(x):
            return any((s << 1) == total for s in accumulate(sum(row) for row in x))
        return helper(grid) or helper(zip(*grid))