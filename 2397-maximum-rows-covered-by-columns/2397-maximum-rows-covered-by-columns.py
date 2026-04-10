class Solution:
    def maximumRows(self, matrix: List[List[int]], numSelect: int) -> int:
        m, n = len(matrix), len(matrix[0])

        res = 0
        nums = [int("".join(map(str, row)), 2) for row in matrix]

        def max_rows(x):
            nonlocal res
            res = max(res, sum(num == (num & x) for num in nums))

        def dfs(i, k, curr):
            if k == 0:
                max_rows(curr)
                return
            for j in range(i, n):
                dfs(j + 1, k - 1, curr | (1 << j))

        dfs(0, numSelect, 0)

        return res