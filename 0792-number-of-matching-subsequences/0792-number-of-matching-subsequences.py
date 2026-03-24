class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        indices = defaultdict(list)
        for i, c in enumerate(s):
            indices[c].append(i)

        def is_subsequence(w):
            idx = -1
            for ch in w:
                idx_list = indices[ch]
                if not idx_list or idx_list[-1] < idx:
                    return False
                idx = idx_list[bisect.bisect_left(idx_list, idx)] + 1
            return True

        return sum(is_subsequence(word) for word in words)