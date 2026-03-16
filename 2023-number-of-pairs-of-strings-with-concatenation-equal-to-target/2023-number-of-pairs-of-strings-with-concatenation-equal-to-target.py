class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        count = Counter(nums)
        n = len(target)
        res = 0
        for num1, f1 in count.items():
            l = len(num1)
            if l >= n:
                continue
            if num1 == target[:l]:
                num2 = target[l:]
                if num1 == num2:
                    res += f1 * (f1 - 1)
                else:
                    f2 = count[num2]
                    res += f1 * f2
        return res