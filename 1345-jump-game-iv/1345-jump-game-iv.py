class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        if n < 2:
            return 0
        graph = defaultdict(list)
        for i, v in enumerate(arr):
            graph[v].append(i)
        q = deque([0])
        visited = [False] * n
        visited[0] = True
        steps = 0
        while q:
            for _ in range(len(q)):
                i = q.popleft()
                v = arr[i]
                for j in graph[v] + [i - 1, i + 1]:
                    if 0 < j < n and not visited[j]:
                        if j == n - 1:
                            return steps + 1
                        q.append(j)
                        visited[j] = True
                graph[v].clear()
            steps += 1
        return -1

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna