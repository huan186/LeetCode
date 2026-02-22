class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        mapping = {order[i] : chr(i + 97) for i in range(len(order))}
        def convert(s):
            return ''.join(mapping[c] for c in s)
        for i in range(len(words)):
            words[i] = convert(words[i])
        for i in range(len(words) - 1):
            if words[i] > words[i + 1]:
                return False
        return True