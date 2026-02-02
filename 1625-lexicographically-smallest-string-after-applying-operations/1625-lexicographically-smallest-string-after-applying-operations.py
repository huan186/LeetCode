class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        from collections import deque

        seen = set()
        q = deque([s])
        res = s

        while q:
            cur = q.popleft()
            if cur in seen:
                continue
            seen.add(cur)

            res = min(res, cur)

            lst = list(cur)
            for i in range(1, len(lst), 2):
                lst[i] = str((int(lst[i]) + a) % 10)
            add_str = ''.join(lst)

            rot_str = cur[-b:] + cur[:-b]

            q.append(add_str)
            q.append(rot_str)

        return res
