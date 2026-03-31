class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        n = len(security)
        postfix = [1] * n
        for i in range(n - 2, -1, -1):
            if security[i] <= security[i + 1]:
                postfix[i] = postfix[i + 1] + 1
        res = []
        desc = 0
        for i in range(n - time):
            if i == 0 or security[i] > security[i - 1]:
                desc = 1
            else:
                desc += 1
            if i >= time and desc > time and postfix[i] > time:
                res.append(i)
        return res