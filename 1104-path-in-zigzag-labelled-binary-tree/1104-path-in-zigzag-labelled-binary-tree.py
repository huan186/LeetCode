class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        r = label.bit_length()

        def helper(l):
            return  (1 << r) + (1 << (r - 1)) - l - 1
        n = label if r % 2 else helper(label)
        res = []
        while n > 0:
            res.append(n if r % 2 else helper(n))
            r -= 1
            n >>= 1
        return res[::-1]