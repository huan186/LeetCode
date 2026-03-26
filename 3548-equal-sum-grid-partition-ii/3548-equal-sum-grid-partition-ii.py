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
                l1, l2 = pos[diff], pos[-diff]
                if (
                        diff == 0
                        or (n == 1 and (
                                (diff > 0 and (x[0][0] == diff or x[i][0] == diff))
                                or (diff < 0 and (x[i + 1][0] == -diff or x[-1][0] == -diff)))
                        ) or (n != 1 and (
                                    (diff > 0 and l1 and l1[0][p] <= i and (l1[0][1 - p] == 0 or l1[0][1 - p] == n - 1 or i > 0))
                                or (diff < 0 and l2 and l2[-1][p] > i and (l2[-1][1 - p] == 0 or l2[-1][1 - p] == n - 1 or i < m - 2))))
                ):
                    return True
            return False

        return helper(grid, 0) or helper(list(zip(*grid)), 1)