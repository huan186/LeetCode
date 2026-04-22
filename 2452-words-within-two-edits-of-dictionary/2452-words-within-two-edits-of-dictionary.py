class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        res = []
        for q in queries:
            for d in dictionary:
                cnt = 0
                for a, b in zip(q, d):
                    if a != b:
                        cnt += 1
                    if cnt > 2:
                        break
                else:
                    res.append(q)
                    break
        return res