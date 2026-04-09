class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        bits = [0] * 21
        for num in nums:
            for i in range(21):
                bits[i] ^= num & 1
                num >>= 1
        res = 0
        for i in range(21):
            if bits[i] != k & 1:
                res += 1
            k >>= 1
        print(bits)
        return res