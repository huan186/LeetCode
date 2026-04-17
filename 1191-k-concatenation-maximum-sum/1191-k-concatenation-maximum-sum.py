class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        mod = 10 ** 9 + 7
        n = len(arr)
        x = []
        s = 0
        tot = 0
        for num in arr:
            s += num
            tot += num
            if s < 0:
                s = 0
            x.append(s)

        if k == 1:
            return max(x) % mod
        
        s = 0
        for num in arr[::-1]:
            s += num
            if s < 0:
                s = 0

        return max(max(x), x[-1] + s + max(0, (k - 2) * tot)) % mod


            