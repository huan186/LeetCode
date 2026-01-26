class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        freq = Counter()
        cnt = Counter()
        res = 0

        for i, x in enumerate(nums):
            f = freq[x]
            if f:
                cnt[f] -= 1
                if cnt[f] == 0:
                    del cnt[f]

            freq[x] += 1
            cnt[freq[x]] += 1

            if (
                len(cnt) == 1 and (1 in cnt or cnt[next(iter(cnt))] == 1)
                or len(cnt) == 2 and (
                    1 in cnt and cnt[1] == 1
                    or max(cnt) == min(cnt) + 1 and cnt[max(cnt)] == 1
                )
            ):
                res = i + 1

        return res
