class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        cnt = [0] * 3
        l = 0
        ans = 0

        for r, ch in enumerate(s):
            cnt[ord(ch) - ord('a')] += 1

            if all(c > 0 for c in cnt):
                while cnt[ord(s[l]) - ord('a')] > 1:
                    cnt[ord(s[l]) - ord('a')] -= 1
                    l += 1

                ans += l + 1

        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna