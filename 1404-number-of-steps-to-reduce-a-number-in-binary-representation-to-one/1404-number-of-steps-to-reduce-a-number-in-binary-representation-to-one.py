class Solution:
    def numSteps(self, s: str) -> int:
        operations = 0
        carry = 0
        for c in reversed(s[1:]):
            digit = int(c) + carry
            if digit % 2 == 1:
                operations += 2
                carry = 1
            else:
                operations += 1

        return operations + carry