class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort(key=lambda x: (len(x), x), reverse=False)
        word_set = {''}
        i, n, l = 0, len(words), 0
        res = ''
        while word_set:
            l += 1
            found = False
            temp = set()
            while i < n and len(words[i]) <= l:
                if words[i][:-1] in word_set:
                    if not found:
                        res = words[i]
                        found = True
                    temp.add(words[i])
                i += 1
            word_set = temp
        return res