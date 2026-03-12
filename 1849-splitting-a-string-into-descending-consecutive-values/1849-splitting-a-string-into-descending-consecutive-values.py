class Solution:
    def splitString(self, s: str) -> bool:
        n = len(s)

        def dfs(start, prev, parts):
            if start == n:
                return parts > 1
            for end in range(start + 1, n + 1):
                v = int(s[start: end])
                if prev != -1 and v >= prev:
                    break
                if (prev == -1 or v == prev - 1) and dfs(end, v, parts + 1):
                    return True
            return False

        return dfs(0, -1, 0)