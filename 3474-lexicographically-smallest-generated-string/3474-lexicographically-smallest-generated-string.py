class Solution:
    def generateString(self, str1: str, str2: str) -> str:
        n, m = len(str1), len(str2)
        arr2 = list(str2)
        res = [''] * (m + n - 1)
        replaceable = [True] * (m + n - 1)
        for i, c in enumerate(str1):
            if c == 'T':
                for j in range(m):
                    if res[i + j] == '':
                        res[i + j] = str2[j]
                    elif res[i + j] != str2[j]:
                        return ''
                    replaceable[i + j] = False
        for i, c in enumerate(res):
            if c == '':
                res[i] = 'a'
        for i, c in enumerate(str1):
            if c == 'T' or res[i : i + m] != arr2:
                continue
            for j in range(i + m - 1, i - 1, -1):
                if replaceable[j]:
                    res[j] = 'b'
                    break
            else:
                return ''

        return ''.join(res)