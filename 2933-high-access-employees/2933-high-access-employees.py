class Solution:
    def findHighAccessEmployees(self, access_times: List[List[str]]) -> List[str]:
        a = defaultdict(list)
        for name, t in access_times:
            h, m = int(t[:2]), int(t[2:])
            a[name].append(h * 60 + m)
        res = []
        for name, lst in a.items():
            lst.sort()
            for i in range(2, len(lst)):
                if lst[i] - lst[i - 2] < 60:
                    res.append(name)
                    break
        return res


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna