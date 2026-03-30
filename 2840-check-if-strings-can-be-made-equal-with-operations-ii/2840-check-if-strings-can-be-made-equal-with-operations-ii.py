class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        count_even = Counter()
        count_odd = Counter()
        i = 0
        for i, (c1, c2) in enumerate(zip(s1, s2)):
            if i % 2 == 0:
                count_even[c1] += 1
                count_even[c2] -= 1
            else:
                count_odd[c1] += 1
                count_odd[c2] -= 1
        def ok(count):
            return all(f == 0 for f in count.values())
        return ok(count_even) and ok(count_odd)