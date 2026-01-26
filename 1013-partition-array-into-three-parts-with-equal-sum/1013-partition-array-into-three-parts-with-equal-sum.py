class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        total = sum(arr)
        if total % 3 != 0:
            return False
        s, cnt, target = 0, 0, total // 3
        for num in arr:
            s += num
            if s == target:
                cnt += 1
                s = 0
                if cnt == 3: return True
        return False
