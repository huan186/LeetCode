class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        height = [0] * n
        res = 0
        
        for row in matrix:
            for i in range(n):
                height[i] = height[i] + 1 if row[i] == 1 else 0
            
            count = [0] * (m + 1)
            for h in height:
                count[h] += 1
            
            width = 0
            for h in range(m, 0, -1):
                width += count[h]
                res = max(res, width * h)
        
        return res