class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        res = []
        n = len(num)
        def dfs(start, expression, value, last):
            if start == n:
                if value == target:
                    res.append(expression)
                return

            for end in range(start, n):
                if end > start and num[start] == '0':
                    break
                cur = int(num[start:end + 1])
                if start == 0:
                    dfs(end + 1, str(cur), cur, cur)
                else:
                    dfs(end + 1, expression + "+" + str(cur), value + cur, cur)
                    dfs(end + 1, expression + "-" + str(cur), value - cur, -cur)
                    dfs(end + 1, expression + "*" + str(cur), value - last + last * cur, last * cur)
            
        dfs(0, "", 0, 0)
        return res