class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        def find_all(x, y):
            res = []
            i = x.find(y)
            while i != -1:
                res.append(i)
                i = x.find(y, i + 1)
            return res
        ia = find_all(s, a)
        ib = find_all(s, b)
        if not ia or not ib:
            return []
        res = []
        iib = 0
        for i in ia:
            while iib < len(ib) and i - ib[iib] > k:
                iib += 1
            if iib < len(ib) and abs(i - ib[iib]) <= k:
                res.append(i)
        return res