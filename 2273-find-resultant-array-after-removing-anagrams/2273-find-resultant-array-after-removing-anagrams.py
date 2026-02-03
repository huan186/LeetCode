class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        ans = []
        prev_cnt = Counter()

        for word in words:
            cnt = Counter(word)
            if cnt != prev_cnt:
                prev_cnt = cnt
                ans.append(word)


        return ans