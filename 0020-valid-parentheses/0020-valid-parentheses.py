class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {
            '(': ')',
            '{': '}',
            '[': ']',
        }

        st = []

        for c in s:
            if c in '({[':
                st.append(mapping[c])
            else:
                if not st or st.pop() != c:
                    return False

        return len(st) == 0

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna