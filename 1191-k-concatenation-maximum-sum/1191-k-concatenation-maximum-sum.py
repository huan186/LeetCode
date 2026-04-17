class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        mod = 10 ** 9 + 7
        n = len(arr)
        best = suff = 0
        tot = 0
        for num in arr:
            suff += num
            tot += num
            suff = max(suff, 0)
            best = max(best, suff)

        if k == 1:
            return best % mod
        
        pref = 0
        for num in arr[::-1]:
            pref += num
            pref = max(pref, 0)

        return max(best, pref + suff + max(0, (k - 2) * tot)) % mod