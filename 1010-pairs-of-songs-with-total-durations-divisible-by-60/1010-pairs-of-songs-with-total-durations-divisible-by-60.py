class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        cnt = [0] * 60
        res = 0
        for t in time:
            r = t % 60
            res += cnt[(60 - r) % 60]
            cnt[r] += 1
        return res