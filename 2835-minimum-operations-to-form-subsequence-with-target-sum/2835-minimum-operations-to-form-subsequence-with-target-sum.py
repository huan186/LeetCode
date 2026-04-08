class Solution:
    def minOperations(self, nums: List[int], target: int) -> int:
        s = sum(nums)
        if s < target:
            return -1
        res = 0
        nums.sort()
        while target:
            num = nums.pop()
            if s - num >= target:
                s -= num
            elif num <= target:
                s -= num
                target -= num
            else:
                res += 1
                nums.append(num >> 1)
                nums.append(num >> 1)
        return res