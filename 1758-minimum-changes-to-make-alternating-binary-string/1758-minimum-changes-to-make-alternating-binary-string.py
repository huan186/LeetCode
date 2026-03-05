class Solution:
    def minOperations(self, s: str) -> int:
        ops = 0
        for i, c in enumerate(s):
            if (i % 2) == (c == '0'):
                ops += 1
        return min(ops, len(s) - ops)