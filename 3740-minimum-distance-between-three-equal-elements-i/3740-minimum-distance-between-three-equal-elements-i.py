class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        n = len(nums)
        res = inf
        indices = [[-1] * 2 for _ in range(n + 1)]
        for i, num in enumerate(nums):
            if indices[num][0] == -1:
                indices[num][0] = i
            elif indices[num][1] == -1:
                indices[num][1] = i
            else:
                res = min(res, 2 * (i - indices[num][0]))
                indices[num][0], indices[num][1] = indices[num][1], i
        return res if res != inf else -1