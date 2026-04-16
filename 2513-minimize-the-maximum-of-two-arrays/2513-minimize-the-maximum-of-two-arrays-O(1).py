class Solution:
    def minimizeSet(self, d1, d2, c1, c2):
        def f(d, c):
            return c + (c - 1) // (d - 1)
        return max(f(d1, c1), f(d2, c2), f(lcm(d1, d2), c1 + c2))