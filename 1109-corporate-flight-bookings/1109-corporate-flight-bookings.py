class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        s = [0] * (n + 1)
        for first, last, seats in bookings:
            s[first - 1] += seats
            s[last] -= seats
        for i in range(1, n):
            s[i] += s[i - 1]
        return s[:-1]