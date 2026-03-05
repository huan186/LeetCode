class Solution:
    def countWays(self, ranges: List[List[int]]) -> int:
        mod = 10 ** 9 + 7
        ranges.sort()
        cnt = 0
        prev_end = -1
        for start, end in ranges:
            if prev_end < start:
                cnt += 1
            prev_end = max(prev_end, end)
        return (2 ** cnt) % mod