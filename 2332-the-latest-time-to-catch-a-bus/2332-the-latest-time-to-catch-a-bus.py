class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        heapq.heapify(buses)
        heapq.heapify(passengers)
        prev = 0
        res = 0
        while buses and passengers:
            b = heapq.heappop(buses)
            c = 0
            while passengers and c < capacity and passengers[0] <= b:
                p = heapq.heappop(passengers)
                if p - 1 != prev:
                    res = p - 1
                prev = p
                c += 1
            if c < capacity and prev != b:
                res = b
        return res