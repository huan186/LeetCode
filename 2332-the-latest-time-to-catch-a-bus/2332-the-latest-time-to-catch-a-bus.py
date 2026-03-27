class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        buses.sort()
        passengers.sort()
        res = 0
        i, j, m, n = 0, 0, len(buses), len(passengers)
        while i < m:
            c = 0
            while j < n and c < capacity and passengers[j] <= buses[i]:
                if j == 0 or passengers[j] - 1 != passengers[j - 1]:
                    res = passengers[j] - 1
                c += 1
                j += 1
            if c < capacity and passengers[j - 1] != buses[i]:
                res = buses[i]
            i += 1
        return res