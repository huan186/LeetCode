class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        seen = {}
        res = inf
        for i, num in enumerate(nums):
            if num in seen:
                res = min(res, i - seen[num])
            seen[int(str(num)[::-1])] = i
        return res if res != inf else -1