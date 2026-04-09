class Solution:
    def resultingString(self, s: str) -> str:
        st = []
        def consecutive(a, b):
            i1, i2 = ord(a), ord(b)
            d = abs(i1 - i2)
            return d == 1 or d == 25
        for c in s:
            if st and consecutive(c, st[-1]):
                st.pop()
            else:
                st.append(c)
        return "".join(st)