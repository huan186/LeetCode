class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        total = sum(sum(row) for row in grid)
        def helper(x):
            s = 0
            for row in x:
                s += sum(row)
                d = (s << 1) - total
                if d == 0:
                    return True
                if d > 0:
                    return False
            return False
        return helper(grid) or helper(zip(*grid))