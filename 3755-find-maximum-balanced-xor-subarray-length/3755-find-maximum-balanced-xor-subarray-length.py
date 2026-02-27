class Solution:
    def maxBalancedSubarray(self, nums: List[int]) -> int:
        seen = {(0, 0): -1}  # value, evens - odds, index
        xor = 0
        diff = 0
        ans = 0
        for i in range(len(nums)):
            xor ^= nums[i]
            diff += 1 if nums[i] % 2 == 0 else -1
            if (xor, diff) in seen:
                ans = max(ans, i - seen[(xor, diff)])
            else:
                seen[(xor, diff)] = i
        return ans
            