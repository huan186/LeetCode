class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        mapping = {order[i] : i for i in range(len(order))}
        def is_smaller(s1, s2):
            l1, l2 = len(s1), len(s2)
            for i in range(min(l1, l2)):
                d = mapping[s2[i]] - mapping[s1[i]]
                if d > 0:
                    return True
                if d < 0:
                    return False
            return l1 <= l2
        for i in range(len(words) - 1):
            if not is_smaller(words[i], words[i + 1]):
                return False
        return True