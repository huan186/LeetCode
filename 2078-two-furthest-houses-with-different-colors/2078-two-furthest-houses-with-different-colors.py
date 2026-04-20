class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)
        for i in range(n - 1, 0, -1):
            if colors[i] != colors[0]:
                res = i
                break
        for i in range(n - 1):
            if colors[i] != colors[-1]:
                res = max(res, n - i - 1)
                break
        return res