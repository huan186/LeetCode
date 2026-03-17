class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        n = len(matrix[0])
        height = [0] * n
        res = 0
        for row in matrix:
            for i in range(n):
                height[i] = 0 if row[i] == 0 else height[i] + 1
            temp = height[:]
            temp.sort()
            for i in range(n):
                res = max(res, (n - i) * temp[i])
        return res
