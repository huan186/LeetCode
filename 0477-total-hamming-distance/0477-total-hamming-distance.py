class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        ans, n = 0, len(nums)
        for i in range(30):
            bit_cnt = 0
            for num in nums:
                bit_cnt += (num >> i) & 1
            ans += bit_cnt * (n - bit_cnt)
        return ans
                