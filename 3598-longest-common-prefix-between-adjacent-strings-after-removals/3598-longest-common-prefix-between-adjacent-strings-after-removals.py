class Solution:
    def longestCommonPrefix(self, words: List[str]) -> List[int]:
        def common_prefix_len(a, b):
            cnt = 0
            for c1, c2 in zip(a, b):
                if c1 != c2:
                    break
                cnt += 1
            return cnt

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

        def find_max(mx, mn, add):
            if mx != top1:
                return max(top1, add)
            if mn != top2:
                return max(top2, add)
            return max(top3, add)

        res = [0] * n

        for i in range(n):
            e1 = -1 if i == 0 else adj[i - 1]
            e2 = -1 if i == n - 1 else adj[i]
            a = -1 if i == 0 or i == n - 1 else common_prefix_len(words[i - 1], words[i + 1])
            res[i] = find_max(max(e1, e2), min(e1, e2), a)
        return res