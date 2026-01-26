class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        res = energy = sum(t[0] for t in tasks)
        heap = []
        for task in tasks:
            heapq.heappush(heap, (task[0] - task[1], task[0], task[1]))
        while heap:
            _, actual, minimum = heapq.heappop(heap)
            if energy < minimum:
                res += minimum - energy
                energy = minimum - actual
            else:
                energy -= actual
        return res