class PrefixTree:
    def __init__(self):
        self.children = {}
        self.is_end = False

    def add(self, word):
        curr = self
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = PrefixTree()
            curr = curr.children[ch]
        curr.is_end = True

    def search(self, word):
        return self.__search(word, 0, self, 2)

    def __search(self, word, i, node, remain):
        if i == len(word):
            return node.is_end

        for ch in node.children:
            nr = remain if ch == word[i] else remain - 1
            if nr >= 0 and self.__search(word, i + 1, node.children[ch], nr):
                return True

        return False

class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        prefix_dict = PrefixTree()
        for word in dictionary:
            prefix_dict.add(word)
        return [q for q in queries if prefix_dict.search(q)]