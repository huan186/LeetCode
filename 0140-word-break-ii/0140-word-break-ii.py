class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        n = len(s)
        words = set(wordDict)
        
        @lru_cache(None)
        def dfs(i):
            segments = []
            for j in range(i, n):
                w = s[i : j + 1]
                if w not in words:
                    continue
                if j == n - 1:
                    segments.append(w)
                    continue
                rest = dfs(j + 1)
                for r in rest:
                    segments.append('{} {}'.format(w, r))
            return segments
        return dfs(0)
            