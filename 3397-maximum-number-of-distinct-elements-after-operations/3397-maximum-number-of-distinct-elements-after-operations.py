class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        cnt = 0
        prev = - 10 ** 18
        for num in nums:
            if num + k == prev:
                continue
            prev = max(prev + 1, num - k)
            cnt += 1
        return cnt
            