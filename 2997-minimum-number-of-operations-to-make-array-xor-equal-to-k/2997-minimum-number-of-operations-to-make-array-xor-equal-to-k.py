class Solution:
    def minOperations(self, nums: List[int], k: int) -> int: 
        for num in nums:
            k ^= num
        return k.bit_count()