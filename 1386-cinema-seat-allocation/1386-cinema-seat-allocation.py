class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        cnt = defaultdict(set)
        for r, c in reservedSeats:
            if c == 1 or c == 10:
                continue
            if c < 4:
                cnt[r].add(0)
            elif c < 6:
                cnt[r].add(0)
                cnt[r].add(1)
            elif c < 8:
                cnt[r].add(1)
                cnt[r].add(2)
            else:
                cnt[r].add(2)
        print(cnt)
        return 2 * n - sum(2 if len(row) == 3 else 1 for row in cnt.values())
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna