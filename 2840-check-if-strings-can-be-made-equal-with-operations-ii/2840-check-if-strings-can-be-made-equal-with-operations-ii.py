class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        count_even = [0] * 26
        count_odd = [0] * 26
        i = 0
        for i, (c1, c2) in enumerate(zip(s1, s2)):
            idx1, idx2 = ord(c1) - 97, ord(c2) - 97
            if i % 2 == 0:
                count_even[idx1] += 1
                count_even[idx2] -= 1
            else:
                count_odd[idx1] += 1
                count_odd[idx2] -= 1
        return all(c == 0 for c in (count_even + count_odd))