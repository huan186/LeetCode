class Solution:
    def minSideJumps(self, obstacles: list[int]) -> int:
        j = [1, 0, 1]
        p = 0
        for o in obstacles:
            if not o:
                if p:
                    j[p - 1] = min(j[p % 3], j[(p + 1) % 3]) + 1
                continue
            l1, l2 = o % 3, (o + 1) % 3
            j[l1], j[l2] = min(j[l1], j[l2] + 1), min(j[l2], j[l1] + 1)
            j[o - 1] = inf
            p = o
        return min(j)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna