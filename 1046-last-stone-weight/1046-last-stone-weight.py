class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-s for s in stones]
        heapq.heapify(heap)
        while len(heap) >= 2:
            b = heapq.heappop(heap)
            a = heapq.heappop(heap)
            if b < a:
                heapq.heappush(heap, b - a)
        return -heap[0] if heap else 0