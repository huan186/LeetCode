class Solution:
    def minimizeConcatenatedLength(self, words: List[str]) -> int:
        inf = float('inf')
        pairs = {}
        w0 = words[0]
        pairs[(w0[0], w0[-1])] = len(w0)
        for w in words[1:]:
            s1, e1, l = w[0], w[-1], len(w)
            nxt = {}
            for (s2, e2), v in pairs.items():
                nxt[(s1, e2)] = min(nxt.get((s1, e2), inf), v + l - (1 if e1 == s2 else 0))
                nxt[(s2, e1)] = min(nxt.get((s2, e1), inf), v + l - (1 if s1 == e2 else 0))
            pairs = nxt
        return min(pairs.values())
