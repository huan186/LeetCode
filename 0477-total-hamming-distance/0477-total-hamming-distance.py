class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        ans, n = 0, len(nums)
        for i in range(max(nums).bit_length()):
            cnt = 0
            for num in nums:
                cnt += (num >> i) & 1
            ans += cnt * (n - cnt)
        return ans
                