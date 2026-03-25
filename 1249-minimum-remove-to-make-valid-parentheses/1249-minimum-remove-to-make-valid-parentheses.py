class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        q = deque()
        eliminated = set()
        for i, c in enumerate(s):
            if c == '(':
                q.append(i)
            elif c == ')':
                if not q:
                    eliminated.add(i)
                else:
                    q.popleft()
        eliminated.update(q)
        return ''.join(c for i, c in enumerate(s) if i not in eliminated)