class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        heap = [(w, 1, w) for w in workerTimes]
        heapq.heapify(heap)
        res = 0
        for _ in range(mountainHeight):
            t, h, w = heapq.heappop(heap)
            res = t
            heapq.heappush(heap, (t + (h + 1) * w, h + 1, w))
        return res