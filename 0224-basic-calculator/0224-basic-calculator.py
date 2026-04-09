class Solution:
    def calculate(self, s: str) -> int:
        stack = [1]
        sign = 1
        res = 0
        i = 0
        n = len(s)
        while i < n:
            c = s[i]
            if c == ' ':
                i += 1
            elif c == '+':
                sign = stack[-1]
                i += 1
            elif c == '-':
                sign = -stack[-1]
                i += 1
            elif c == '(':
                stack.append(sign)
                i += 1
            elif c == ')':
                stack.pop()
                i += 1
            else:
                num = 0
                while i < n and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1
                res += sign * num
        return res
