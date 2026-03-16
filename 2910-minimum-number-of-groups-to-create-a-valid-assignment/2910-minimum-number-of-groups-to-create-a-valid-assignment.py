class Solution:
    def minGroupsForValidAssignment(self, balls: List[int]) -> int:
        count = Counter(balls)
        minf = min(count.values())

        for k in range(minf, 0, -1):
            boxes = 0
            ok = True

            for f in count.values():
                mn = (f + k) // (k + 1)
                mx = f // k

                if mn > mx:
                    ok = False
                    break

                boxes += mn

            if ok:
                return boxes