from collections import defaultdict
import bisect

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        indices = defaultdict(list)
        for i, c in enumerate(s):
            indices[c].append(i)

        def is_subsequence(w):
            idx = -1
            for ch in w:
                idx_list = indices[ch]
                if not idx_list:
                    return False
                pos = bisect.bisect_right(idx_list, idx)
                if pos == len(idx_list):
                    return False
                idx = idx_list[pos]
            return True

        return sum(is_subsequence(word) for word in words)