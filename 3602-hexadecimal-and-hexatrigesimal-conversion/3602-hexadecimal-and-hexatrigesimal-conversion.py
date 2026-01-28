class Solution:
    def concatHex36(self, n: int) -> str:
        def base_10_to_base_x(x, v10):
            if v10 == 0:
                return '0'
            vx = ''
            while v10 > 0:
                r = v10 % x
                ch = str(r) if r < 10 else chr(ord('A') + r - 10)
                vx = ch + vx
                v10 //= x
            return vx
        return base_10_to_base_x(16, n ** 2) + base_10_to_base_x(36, n ** 3)