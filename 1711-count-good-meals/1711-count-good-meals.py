class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        res = 0
        freq = Counter(deliciousness)
        for d, f in freq.items():
            for i in range(22):
                c = (1 << i) - d
                if c < d:
                    continue
                elif c == d:
                    res += f * (f - 1) // 2
                elif c in freq:
                    res += f * freq[c]
        return res % (10 ** 9 + 7)