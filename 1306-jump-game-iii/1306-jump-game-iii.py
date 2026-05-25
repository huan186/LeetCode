class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        if arr[start] == 0:
            return True
        n = len(arr)
        visited = {start}
        q = deque([start])
        while q:
            i = q.popleft()
            l = i - arr[i]
            r = i + arr[i]
            if l >= 0 and l not in visited:
                if arr[l] == 0:
                    return True
                q.append(l)
                visited.add(l)
            if r < n and r not in visited:
                if arr[r] == 0:
                    return True
                q.append(r)
                visited.add(r)
        return False

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna