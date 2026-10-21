class Solution:
    def findHighAccessEmployees(self, access_times: List[List[str]]) -> List[str]:
        a = defaultdict(list)
        def to_minutes(raw):
            t = int(raw)
            return t // 100 * 60 + (t % 100)
        for name, raw_time in access_times:
            a[name].append(to_minutes(raw_time))
        res = []
        def high_access(lst):
            if len(lst) < 3:
                return False
            lst.sort()
            for i in range(2, len(lst)):
                if lst[i] - lst[i - 2] < 60:
                    return True
        for name, time_list in a.items():
            if high_access(time_list):
                res.append(name)
        return res


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna