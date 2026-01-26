class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        from collections import Counter

        freq = Counter(nums)
        cnt = Counter(freq.values())

        def valid():
            if len(cnt) == 1:
                f = next(iter(cnt))
                return f == 1 or cnt[f] == 1

            if len(cnt) == 2:
                f1, f2 = min(cnt), max(cnt)
                return (
                    f1 == 1 and cnt[f1] == 1 or
                    f2 == f1 + 1 and cnt[f2] == 1
                )

            return False

        for i in range(len(nums) - 1, -1, -1):
            if valid():
                return i + 1

            x = nums[i]
            f = freq[x]

            cnt[f] -= 1
            if cnt[f] == 0:
                del cnt[f]

            if f == 1:
                del freq[x]
            else:
                freq[x] -= 1
                cnt[f - 1] += 1

        return 1
