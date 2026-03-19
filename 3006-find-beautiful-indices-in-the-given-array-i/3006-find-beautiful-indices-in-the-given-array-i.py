class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        i, j = s.find(a), float('-inf')
        res = []
        while i != -1 and j != -1:
            if abs(i - j) <= k:
                res.append(i)
                i = s.find(a, i + 1)
            elif i > j:
                j = s.find(b, max(i - k, 0))
            else:
                i = s.find(a, j - k)
        return res