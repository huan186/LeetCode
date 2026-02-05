class Solution:
    def makeSubKSumEqual(self, arr: List[int], k: int) -> int:
        ops = 0
        n = len(arr)
        seen = set()
        for i in range(k):
            if i in seen:
                continue
            x = set()
            j = i
            while j not in x:
                x.add(j)
                j = (j + k) % n
            a = [arr[j] for j in x]
            a.sort()
            l, r = 0, len(a) - 1
            while l < r:
                ops += a[r] - a[l]
                l += 1
                r -= 1
            seen.update(x)
        return ops