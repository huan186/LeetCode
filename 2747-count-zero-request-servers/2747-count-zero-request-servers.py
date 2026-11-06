class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        queries = [(q, i) for i, q in enumerate(queries)]
        queries.sort()
        h1, h2 = [], []
        for s, t in logs:
            heapq.heappush(h1, (t, s))

        res = [n] * len(queries)
        count = defaultdict(int)

        for q, i in queries:
            while h1 and h1[0][0] <= q:
                t, s = heapq.heappop(h1)
                heapq.heappush(h2, (t, s))
                count[s] += 1

            while h2 and h2[0][0] < q - x:
                t, s = heapq.heappop(h2)
                count[s] -= 1
                if count[s] == 0:
                    del(count[s])
            
            res[i] -= len(count)

        return res
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna