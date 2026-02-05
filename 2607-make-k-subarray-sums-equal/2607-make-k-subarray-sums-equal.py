class Solution:
    def makeSubKSumEqual(self, arr: List[int], k: int) -> int:
        n = len(arr)
        g = gcd(n, k)
        ops = 0

        for i in range(g):
            group = []
            j = i
            while True:
                group.append(arr[j])
                j = (j + k) % n
                if j == i:
                    break

            group.sort()
            l, r = 0, len(group) - 1
            while l < r:
                ops += group[r] - group[l]
                l += 1
                r -= 1

        return ops
