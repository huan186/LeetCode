class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        def is_a_subset(x, y):
            a, b = len(x), len(y)
            if a > b:
                return False
            i1, i2 = 0, 0
            while i1 < a and i2 < b:
                if x[i1] == y[i2]:
                    i1 += 1
                    i2 += 1
                else:
                    i2 += 1
            return i1 == a
        res = -1
        n = len(strs)
        seen = set()
        for i in range(n):
            if strs[i] in seen:
                continue
            for j in range(n):
                if i == j:
                    continue
                if is_a_subset(strs[i], strs[j]):
                    break
            else:
                res = max(res, len(strs[i]))
            seen.add(strs[i])
        return res