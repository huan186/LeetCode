class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        cnts = [0] * 60
        for t in time:
            cnts[t % 60] += 1
        res = 0
        for i in range(31):
            if i == 0 or i == 30:
                res += cnts[i] * (cnts[i] - 1) // 2
            else:
                res += cnts[i] * cnts[60 - i]
        return res