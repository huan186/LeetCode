class Solution:
    def concatHex36(self, n: int) -> str:
        chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        def base_10_to_base_x(x, v10):
            vx = ''
            while v10 > 0:
                vx = chars[v10 % x] + vx
                v10 //= x
            return vx
        return base_10_to_base_x(16, n ** 2) + base_10_to_base_x(36, n ** 3)