class Solution:
    def sortSentence(self, s: str) -> str:
        splits = s.split(' ')
        words = [None] * len(splits)
        for w in splits:
            words[int(w[-1]) - 1] = w[:-1]
        return ' '.join(words)