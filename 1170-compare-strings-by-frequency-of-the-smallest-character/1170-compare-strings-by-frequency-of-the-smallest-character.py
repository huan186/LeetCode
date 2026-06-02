class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def f(s):
            freq = [0] * 26
            for c in s:
                freq[ord(c) - ord('a')] += 1
            for i in range(26):
                if freq[i] != 0:
                    return freq[i]
            return 0
        m = len(queries)
        n = max(len(w) for w in words) + 1
        pref = [0] * n
        for word in words:
            pref[f(word)] += 1
        for i in range(1, n):
            pref[i] += pref[i - 1]
        res = [0] * m
        for i in range(m):
            fq = f(queries[i])
            res[i] = pref[n - 1] - pref[fq]
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna