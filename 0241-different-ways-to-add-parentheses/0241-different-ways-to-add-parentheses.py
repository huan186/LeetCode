class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        nums = []
        ops = []
        cur = 0
        for c in expression:
            if c.isdigit():
                cur = cur * 10 + int(c)
            else:
                nums.append(cur)
                ops.append(c)
                cur = 0
        nums.append(cur)

        def operate(o1, o2, op):
            return o1 + o2 if op == '+' else o1 - o2 if op == '-' else o1 * o2

        @cache
        def compute(l, r):
            return [operate(o1, o2, ops[i - 1])
                    for i in range(l + 1, r + 1)
                    for o1 in compute(l, i - 1)
                    for o2 in compute(i, r)] if l < r else [nums[l]]

        return compute(0, len(nums) - 1)