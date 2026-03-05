class Solution:
    def minOperations(self, s: str) -> int:
        return max((ord('a') - ord(c)) % 26 for c in s)