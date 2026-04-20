class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        res = -1
        for i in range(len(colors) - 1):
            for j in range(len(colors) - 1, i, -1):
                if colors[i] != colors[j]:
                    res = max(res, j - i)
                    break
        return res