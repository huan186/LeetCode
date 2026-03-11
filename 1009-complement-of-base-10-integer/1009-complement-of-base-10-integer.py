class Solution:
    def bitwiseComplement(self, n: int) -> int:
        return 1 if n == 0 else (1 << n.bit_length()) - n - 1