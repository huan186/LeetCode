class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        m, n = len(houses), len(heaters)

        def possible(r):
            i, j, = 0, 0
            while i < m and j < n:
                if abs(houses[i] - heaters[j]) <= r:
                    i += 1
                else:
                    j += 1
            return i == m

        
        left, right = 0, 10 ** 9

        while left < right:
            mid = (left + right) // 2
            if possible(mid):
                right = mid
            else:
                left = mid + 1
        
        return left