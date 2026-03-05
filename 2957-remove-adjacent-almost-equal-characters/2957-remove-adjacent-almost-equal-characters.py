class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        return (sum(abs(ord(a) - ord(b)) <= 1 for a, b in zip(word[:-1], word[1:])) + 1) // 2