class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        n = len(intervals)
        i = 0
        while i < n:
            start, end = intervals[i][0], intervals[i][1]
            j = i + 1
            while j < n and intervals[j][0] <= end:
                end = max(end, intervals[j][1])
                j += 1
            res.append([start, end])
            i = j
        return res