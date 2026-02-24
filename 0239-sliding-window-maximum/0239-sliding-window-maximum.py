class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        heap = []
        freq = Counter()
        for i, v in enumerate(nums):
            freq[v] += 1
            heapq.heappush(heap, -v)
            if i + 1 >= k:
                while freq[-heap[0]] == 0:
                    heapq.heappop(heap)
                res.append(-heap[0])
                freq[nums[i - k + 1]] -= 1
        return res