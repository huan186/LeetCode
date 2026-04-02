class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m, n = len(matrix), len(matrix[0])
        def valid(r, c):
            v = matrix[r][c]
            while r < m and c < n:
                if matrix[r][c] != v:
                    return False
                r += 1
                c += 1
            return True
        for i in range(m - 1):
            if not valid(i, 0):
                return False
        for j in range(1, n - 1):
            if not valid(0, j):
                return False
        return True