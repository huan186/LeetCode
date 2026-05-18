class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        if n < 2:
            return 0
        idx = defaultdict(list)
        for i, v in enumerate(arr):
            idx[v].append(i)
        q = deque([(0, 0)])
        visited = [False] * n
        visited[0] = True
        while q:
            steps, i = q.popleft()
            v = arr[i]
            for j in idx[v] + [i - 1, i + 1]:
                if 0 < j < n and j != i and not visited[j]:
                    if j == n - 1:
                        return steps + 1
                    q.append((steps + 1, j))
                    visited[j] = True
            idx[v].clear()
        return -1

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna