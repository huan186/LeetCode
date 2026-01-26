class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        total = sum(arr)
        if total % 3 != 0:
            return False
        n, i, target = len(arr), 0, total // 3
        s, cnt = 0, 0
        for num in arr:
            s += num
            if s == target:
                cnt += 1
                s = 0
        return cnt >= 3