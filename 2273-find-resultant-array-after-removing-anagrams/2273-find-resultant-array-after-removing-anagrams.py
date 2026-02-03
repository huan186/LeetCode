class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        ans = []
        prev = -1

        for word in words:
            curr = 0
            for ch in word:
                curr += 11 ** (ord(ch) - 97)
            if curr != prev:
                prev = curr
                ans.append(word)

        return ans