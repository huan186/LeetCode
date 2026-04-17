class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()

        j = 0
        ans = 0
        n = len(heaters)

        for h in houses:
            while j + 1 < n and abs(heaters[j + 1] - h) <= abs(heaters[j] - h):
                j += 1

            ans = max(ans, abs(heaters[j] - h))
        return ans