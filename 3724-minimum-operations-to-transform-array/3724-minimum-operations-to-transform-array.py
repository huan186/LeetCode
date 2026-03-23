class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        ops = 0
        last_ops = float('inf')
        last_num = nums2[-1]
        for num1, num2 in zip(nums1, nums2):
            ops += abs(num1 - num2)
            if num1 >= last_num >= num2 or num1 <= last_num <= num2:
                last_ops = 1
            else:
                last_ops = min(last_ops, min(abs(num1 - last_num), abs(num2 - last_num)) + 1)
        return ops + last_ops