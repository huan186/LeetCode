class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        n = len(capacity)
        heap = [capacity[i] - rocks[i] for i in range(n)]
        heapq.heapify(heap)
        res = 0
        while heap:
            curr = heapq.heappop(heap)
            if curr <= 0:
                res += 1
            elif additionalRocks >= curr:
                res += 1
                additionalRocks -= curr
            else:
                break
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna