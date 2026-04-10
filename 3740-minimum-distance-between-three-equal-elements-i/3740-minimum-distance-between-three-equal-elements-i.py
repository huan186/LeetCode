class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        n = len(nums)
        res = inf
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    if nums[i] == nums[j] == nums[k]:
                        res = min(res, 2 * (k - i))
        return res if res != inf else -1