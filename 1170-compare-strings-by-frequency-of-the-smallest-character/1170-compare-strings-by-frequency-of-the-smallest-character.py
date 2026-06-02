class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def f(s):
            freq = [0] * 26
            for c in s:
                freq[ord(c) - ord('a')] += 1
            for i in range(26):
                if freq[i]:
                    return freq[i]
            return 0

        max_len = max(
            max(len(w) for w in words),
            max(len(q) for q in queries)
        )

        post = [0] * (max_len + 2)

        for word in words:
            post[f(word)] += 1

        for i in range(max_len, -1, -1):
            post[i] += post[i + 1]

        return [post[f(q) + 1] for q in queries]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna