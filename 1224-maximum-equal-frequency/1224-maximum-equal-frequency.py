class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        freq = Counter(nums)

        def valid():
            cnt = Counter(freq.values())
            n = len(cnt)
            min_key, max_key = min(cnt.keys()), max(cnt.keys())
            return (
                    n == 1 and (min_key == 1 or min(cnt.values()) == 1)
                    or n == 2 and (
                            1 in cnt and cnt[1] == 1
                            or max_key - min_key == 1 and cnt[max_key] == 1
                    )
            )

        for i in range(len(nums) - 1, -1, -1):
            if valid():
                return i + 1
            if freq[nums[i]] == 1:
                freq.pop(nums[i])
            else:
                freq[nums[i]] -= 1

        return 1