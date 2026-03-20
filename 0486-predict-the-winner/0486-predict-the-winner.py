class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        nums = tuple(nums)
        @lru_cache(None)
        def max_score(l, r):
            if l == r:
                return nums[l], 0
            if r - l == 1:
                return max(nums[l], nums[r]), min(nums[l], nums[r])

            # take left
            s2l, s1l = max_score(l + 1, r)
            s1l += nums[l]

            # take right
            s2r, s1r = max_score(l, r - 1)
            s1r += nums[r]
            
            return max((s1l, s2l), (s1r, s2r))

        s1, s2 = max_score(0, len(nums) - 1)
        return s1 >= s2