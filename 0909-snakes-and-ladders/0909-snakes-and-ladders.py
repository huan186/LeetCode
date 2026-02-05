class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        target = n * n
        arr = [0]
        for i in range(n):
            r = n - i - 1
            c_range = range(n) if i % 2 == 0 else range(n - 1, -1, -1)
            for c in c_range:
                arr.append(board[r][c])

        q = deque([(0, 1)])
        visited = {1}

        while q:
            steps, curr = q.popleft()
            if curr == target:
                return steps
            for d in range(1, 7):
                nxt = curr + d
                if nxt > target:
                    break
                if arr[nxt] != -1:
                    nxt = arr[nxt]
                if nxt not in visited:
                    q.append((steps + 1, nxt))
                    visited.add(nxt)
        return -1