class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        i, j, m, n = 0, 0, len(word1), len(word2)
        ans = []
        while i < m or j < n:
            if i != m and (
                j == n or
                word1[i] > word2[j] or
                word1[i] == word2[j] and word1[i + 1:] >= word2[j + 1:]
            ):
                ans.append(word1[i])
                i += 1
            else:
                ans.append(word2[j])
                j += 1
        return ''.join(ans)
