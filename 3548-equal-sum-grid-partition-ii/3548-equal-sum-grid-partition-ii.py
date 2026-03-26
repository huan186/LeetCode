class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        pos = defaultdict(list)
        s = 0
        for i, row in enumerate(grid):
            for j, num in enumerate(row):
                pos[num].append((i, j))
                s += num

        def helper(x, p):
            m, n = len(x), len(x[0])
            s1 = 0
            for i, row in enumerate(x[:-1]):
                s1 += sum(x[i])
                diff = 2 * s1 - s
                if diff == 0:
                    return True
                if n == 1:
                    if diff > 0:
                        if x[0][0] == diff or x[i][0] == diff:
                            return True
                    else:
                        if x[i + 1][0] == -diff or x[-1][0] == -diff:
                            return True
                else:
                    if diff > 0:
                        l = pos[diff]
                        if l and l[0][p] <= i and (l[0][1 - p] == 0 or l[0][1 - p] == n - 1 or i > 0):
                            return True
                    else:
                        l2 = pos[-diff]
                        if l2 and l2[-1][p] > i and (l2[-1][1 - p] == 0 or l2[-1][1 - p] == n - 1 or i < m - 2):
                            return True
            return False

        return helper(grid, 0) or helper(list(zip(*grid)), 1)