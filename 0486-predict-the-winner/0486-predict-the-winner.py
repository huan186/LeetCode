class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        @lru_cache(None)
        def diff(l, r):
            if l == r:
                return nums[l]
            if r - l == 1:
                return abs(nums[l] - nums[r])
            return max(nums[l] - diff(l + 1, r), nums[r] - diff(l, r - 1))
        return diff(0, len(nums) - 1) >= 0