class Solution:
    def minGroupsForValidAssignment(self, balls: List[int]) -> int:
        count = Counter(balls)
        res = float('inf')
        for k in range(1, min(count.values()) + 1):
            boxes = 0
            for f in count.values():
                mn = (f + k) // (k + 1)
                mx = f // k
                if mn > mx:
                    break
                boxes += mn
            else:
                res = min(res, boxes)
        return res