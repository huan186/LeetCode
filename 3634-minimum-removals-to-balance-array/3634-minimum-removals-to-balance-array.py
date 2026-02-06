class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        ans = n
        right = 0
        for left in range(n):
            while right < n and nums[left] * k >= nums[right]:
                right += 1
            ans = min(ans, left + n - right)
        return ans