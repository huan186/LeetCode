class Solution:
    def minOperations(self, s: str) -> int:
        for i in range(1, 26):
            if chr(ord('a') + i) in s:
                return 26 - i
        return 0