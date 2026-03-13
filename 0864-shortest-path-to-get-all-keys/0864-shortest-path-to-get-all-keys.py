class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        m, n = len(grid), len(grid[0])
        start = None
        key_cnt = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '@':
                    start = (i, j)
                elif 'a' <= grid[i][j] <= 'f':
                    key_cnt += 1

        start_state = (start[0] << 11) | (start[1] << 6)
        visited = {start_state}

        q = deque([(start_state, 0)])

        while q:
            v, steps = q.popleft()

            x = v >> 11
            y = (v >> 6) & 31
            keys = v & 63

            if keys == (1 << key_cnt) - 1:
                return steps

            for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                nx, ny = x + dx, y + dy

                if not (0 <= nx < m and 0 <= ny < n):
                    continue

                cell = grid[nx][ny]
                if cell == '#':
                    continue

                nkeys = keys

                if 'A' <= cell <= 'F':
                    if not (keys & (1 << (ord(cell) - ord('A')))):
                        continue

                if 'a' <= cell <= 'f':
                    nkeys |= 1 << (ord(cell) - ord('a'))

                nv = (nx << 11) | (ny << 6) | nkeys

                if nv not in visited:
                    visited.add(nv)
                    q.append((nv, steps + 1))

        return -1
