class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        r = [(q / w, q) for q, w in zip(quality, wage)]
        r.sort(reverse=True)
        total_quality = 0
        res = float('inf')
        heap = []
        for i, (x, q) in enumerate(r): # x = quality / wage
            if len(heap) == k:
                total_quality += heapq.heappop(heap)
            total_quality += q
            heapq.heappush(heap, -q)
            if len(heap) == k:
                res = min(res, total_quality / x)
        return res