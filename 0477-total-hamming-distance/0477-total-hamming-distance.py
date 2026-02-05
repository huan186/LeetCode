class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        cnt = [0] * 32
        for num in nums:
            i = 0
            while num > 0:
                cnt[i] += num & 1
                i += 1
                num >>= 1
        res = 0
        n = len(nums)
        return sum(c * (n - c) for c in cnt)
                