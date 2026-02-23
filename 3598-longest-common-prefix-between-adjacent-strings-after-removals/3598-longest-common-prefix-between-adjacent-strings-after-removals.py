class Solution:
    def longestCommonPrefix(self, words: List[str]) -> List[int]:
        def common_prefix_len(a, b):
            for idx, (x, y) in enumerate(zip(a, b)):
                if x != y:
                    return idx
            return min(len(a), len(b))

        n = len(words)
        l1, l2, l3 = 0, 0, 0

        adj_pref_len = [0] * (n - 1)
        for i in range(n - 1):
            cpl = common_prefix_len(words[i], words[i + 1])
            adj_pref_len[i] = cpl
            if cpl >= l1:
                l1, l2, l3 = cpl, l1, l2
            elif cpl >= l2:
                l2, l3 = cpl, l2
            elif cpl > l3:
                l3 = cpl

        res = [0] * n

        for i in range(n):
            eliminate1 = -1 if i == 0 else adj_pref_len[i - 1]
            eliminate2 = -1 if i == n - 1 else adj_pref_len[i]
            take = -1 if i == 0 or i == n - 1 else common_prefix_len(words[i - 1], words[i + 1])
            arr = [l1, l2, l3, take]
            for x in [eliminate1, eliminate2]:
                if x in arr:
                    arr.remove(x)
            res[i] = max(arr)

        return res