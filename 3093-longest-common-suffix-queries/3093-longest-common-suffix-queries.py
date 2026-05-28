class Node:
    def __init__(self):
        self.children = {}
        self.best = (inf, -1)

class Trie:
    def __init__(self):
        self.root = Node()
    
    def add(self, word: str, idx: int):
        l = len(word)
        node = self.root

        if node.best[0] > l:
            node.best = (l, idx)

        for ch in word:
            if ch not in node.children:
                node.children[ch] = Node()
            node = node.children[ch]

            if node.best[0] > l:
                node.best = (l, idx)
    
    def search(self, word: str) -> int:
        node = self.root
        for ch in word:
            if ch not in node.children:
                break
            node = node.children[ch]
        return node.best[1]

class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        trie = Trie()
        for i, word in enumerate(wordsContainer):
            trie.add(word[::-1], i)

        return [trie.search(q[::-1]) for q in wordsQuery]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna