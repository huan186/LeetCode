class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        heap = [(w, 1, w) for w in workerTimes]
        heapq.heapify(heap)
        for _ in range(mountainHeight - 1):
            t, h, w = heapq.heappop(heap)
            heapq.heappush(heap, (t + (h + 1) * w, h + 1, w))
        return heap[0][0]