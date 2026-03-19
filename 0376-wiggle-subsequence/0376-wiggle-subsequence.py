class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        ans = 0
        for a in ([0, 0], [10 ** 18, 0]):
            for num in nums:
                num += 1
                if a[0] <= 0:
                    if num > -a[0]:
                        a[0], a[1] = num, a[1] + 1
                    else:
                        a[0] = -num
                else:
                    if num < a[0]:
                        a[0], a[1] = -num, a[1] + 1
                    else:
                        a[0] = num
            ans = max(ans, a[1])
        return ans