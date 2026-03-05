class Solution:
    def countWays(self, ranges: List[List[int]]) -> int:
        mod = 10 ** 9 + 7
        ranges.sort()
        res = 2
        prev_end = ranges[0][0]
        for start, end in ranges:
            if prev_end < start:
                res = (res << 1) % mod
            prev_end = max(prev_end, end)
        return res