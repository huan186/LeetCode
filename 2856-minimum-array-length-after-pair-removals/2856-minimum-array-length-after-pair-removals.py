class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        counts = Counter(nums)
        heap = [(-v, k) for k, v in counts.items()]
        heapq.heapify(heap)
        c = 0
        while len(heap) > 1:
            v1, k1 = heapq.heappop(heap)
            v2, k2 = heapq.heappop(heap)
            c += 2
            if v1 + 1 < 0:
                heapq.heappush(heap, (v1 + 1, k1))
            if v2 + 1 < 0:
                heapq.heappush(heap, (v2 + 1, k2))
        return len(nums) - c

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna