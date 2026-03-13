class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        left, right = 1, 10 ** 18
        while left < right:
            mid = left + (right - left) // 2

            height = 0

            for wt in workerTimes:
                height += math.floor((-1 + math.sqrt(1 + 8 * mid / wt)) / 2)

            if height >= mountainHeight:
                right = mid
            else:
                left = mid + 1

        return left