class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        ans = []
        prev = -1

        for word in words:
            curr = 0
            for ch in word:
                curr += 2.21 ** (ord(ch) - 97)
            if abs(curr - prev) > 1e-5:
                prev = curr
                ans.append(word)

        return ans