class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        m = max(nums)
        f = [0] * (m + 1)
        for num in nums:
            f[num] += 1
        take = skip = 0
        for i in range(1, m + 1):
            take, skip = max(take, skip + i * f[i]), max(take, skip)
        return max(take, skip)
            