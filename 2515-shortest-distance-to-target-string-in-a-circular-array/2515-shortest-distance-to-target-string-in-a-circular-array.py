class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        res = inf
        n = len(words)
        for i, w in enumerate(words):
            if w == target:
                if i <= startIndex:
                    res = min(res, startIndex - i, i + n - startIndex)
                else:
                    res = min(res, i - startIndex, startIndex + n - i)
        return res if res != inf else -1