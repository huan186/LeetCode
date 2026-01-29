class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        freq = Counter(nums)
        need = Counter()

        for x in nums:
            if not freq[x]:
                continue
            if need[x]:
                need[x] -= 1
                need[x + 1] += 1
                freq[x] -= 1
            else:
                if freq[x + 1] and freq[x + 2]:
                    freq[x] -= 1
                    freq[x + 1] -= 1
                    freq[x + 2] -= 1
                    need[x + 3] += 1
                else:
                    return False

        return True