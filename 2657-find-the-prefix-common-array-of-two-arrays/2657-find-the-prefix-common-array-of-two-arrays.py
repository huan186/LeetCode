class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        seen = set()
        n = len(A)
        res = []
        cnt = 0
        for i in range(n):
            if A[i] == B[i]:
                cnt += 1
            else:
                if A[i] in seen:
                    cnt += 1
                else:
                    seen.add(A[i])
                if B[i] in seen:
                    cnt += 1
                else:
                    seen.add(B[i])
            res.append(cnt)
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna