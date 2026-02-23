class Solution:
    def minimizeResult(self, expression: str) -> str:
        pi = expression.index('+')
        n = len(expression)
        min_evaluation = float('inf')
        res = ''
        for i in range(pi):
            for j in range(pi + 2, n + 1):
                a = 1 if i == 0 else int(expression[:i])
                b = int(expression[i : pi])
                c = int(expression[pi + 1 : j])
                d = 1 if j == n else int(expression[j:])
                evaluation = a * (b + c) * d
                if evaluation < min_evaluation:
                    min_evaluation = evaluation
                    res = expression[:i] + '(' + expression[i : j] + ')' + expression[j:]
        return res