class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        pos = {c: i for i, c in enumerate(order)}
        
        for w1, w2 in zip(words, words[1:]):
            for c1, c2 in zip(w1, w2):
                if pos[c1] < pos[c2]:
                    break
                if pos[c1] > pos[c2]:
                    return False
            else:
                if len(w1) > len(w2):
                    return False
        return True