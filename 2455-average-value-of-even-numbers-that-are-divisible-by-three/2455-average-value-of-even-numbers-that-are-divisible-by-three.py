class Solution:
    def averageValue(self, nums: List[int]) -> int:
        s, cnt = 0, 0
        for num in nums:
            if num % 6 == 0:
                s += num
                cnt += 1
        return 0 if cnt == 0 else s // cnt