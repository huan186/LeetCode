from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        n = len(s)

        if n > 12:
            return res

        def backtrack(start: int, path: List[str]):
            if len(path) == 4:
                if start == n:
                    res.append(".".join(path))
                return

            remaining = n - start
            slots = 4 - len(path)
            if remaining < slots or remaining > slots * 3:
                return

            for length in range(1, 4):
                if start + length > n:
                    break

                part = s[start:start + length]

                if part[0] == '0' and length > 1:
                    break

                num = int(part)
                if num <= 255:
                    backtrack(start + length, path + [part])

        backtrack(0, [])
        return res
