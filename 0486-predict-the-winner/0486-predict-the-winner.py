
class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        nums = tuple(nums)
        @lru_cache(None)
        def max_score(x):
            l = len(x)
            if l == 1:
                return x[0], 0
            if l == 2:
                return max(x), min(x)
            # take left
            s2l, s1l = max_score(x[1:])
            s1l += x[0]

            # take right
            s2r, s1r = max_score(x[:-1])
            s1r += x[-1]

            if s1l >= s1r:
                return s1l, s2l
            return s1r, s2r

        s1, s2 = max_score(nums)
        return s1 >= s2