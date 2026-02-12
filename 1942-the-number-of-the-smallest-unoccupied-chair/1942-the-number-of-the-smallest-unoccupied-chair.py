class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        heap = []
        n = len(times)
        seats = [i for i in range(n)]
        times = [times[i] + [i] for i in range(n)]
        times.sort()
        for start, end, idx in times:
            while heap and heap[0][0] <= start:
                _, chair = heapq.heappop(heap)
                heapq.heappush(seats, chair)
            if idx == targetFriend:
                return heapq.heappop(seats)
            heapq.heappush(heap, (end, heapq.heappop(seats)))
        return -1