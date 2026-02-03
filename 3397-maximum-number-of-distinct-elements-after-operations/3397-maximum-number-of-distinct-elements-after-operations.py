class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        cnt = 0
        prev = - 10 ** 18
        for i in range(n):
            diff = max((prev + 1 - nums[i]), -k)
            if diff > k:
                continue
            cnt += 1
            prev = nums[i] + diff
        return cnt
            