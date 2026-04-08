class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        
        def find_max_len(start: int, end: int, steps) -> List[int]:
            tails = []
            x = [0] * n
            for i in range(start, end, steps):
                pos = bisect.bisect_left(tails, nums[i])
                if pos == len(tails):
                    tails.append(nums[i])
                else:
                    tails[pos] = nums[i]
                x[i] = pos + 1
            return x
        
        inc = find_max_len(0, n, 1)
        dec = find_max_len(n - 1, -1, -1)
        
        return n + 1 - max(inc[i] + dec[i] for i in range(1, n - 1) if inc[i] != 1 and dec[i] != 1)