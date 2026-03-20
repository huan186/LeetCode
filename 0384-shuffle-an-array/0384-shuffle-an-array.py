import random

class Solution:
    def __init__(self, nums):
        self.original = nums[:]

    def reset(self):
        return self.original[:]

    def shuffle(self):
        res = self.original[:]
        n = len(res)
        
        for i in range(n):
            j = random.randint(i, n - 1)
            res[i], res[j] = res[j], res[i]
        
        return res