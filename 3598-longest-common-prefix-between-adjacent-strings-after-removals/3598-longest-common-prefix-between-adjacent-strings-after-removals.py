class Solution:
    def longestCommonPrefix(self, words: List[str]) -> List[int]:
        def common_prefix_len(a, b):
            for idx, (x, y) in enumerate(zip(a, b)):
                if x != y:
                    return idx
            return min(len(a), len(b))

        n = len(words)
        top1, top2, top3 = 0, 0, 0

        adj = [0] * (n - 1)
        for i in range(n - 1):
            cpl = common_prefix_len(words[i], words[i + 1])
            adj[i] = cpl
            if cpl >= top1:
                top1, top2, top3 = cpl, top1, top2
            elif cpl >= top2:
                top2, top3 = cpl, top2
            elif cpl > top3:
                top3 = cpl

        res = [0] * n

        for i in range(n):
            e1 = -1 if i == 0 else adj[i - 1]
            e2 = -1 if i == n - 1 else adj[i]
            a = -1 if i == 0 or i == n - 1 else common_prefix_len(words[i - 1], words[i + 1])

            arr = [top1, top2, top3, a]

            for x in [e1, e2]:
                if x in arr:
                    arr.remove(x)

            res[i] = max(arr)
        return res