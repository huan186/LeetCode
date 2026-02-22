class Solution:
    def sortSentence(self, s: str) -> str:
        splits = s.split(' ')
        words = [''] * len(splits)
        for w in splits:
            idx = int(w[-1]) - 1
            words[idx] = w[:-1]
        return ' '.join(words)