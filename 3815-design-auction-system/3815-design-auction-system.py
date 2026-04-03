import heapq
from collections import defaultdict

class AuctionSystem:

    def __init__(self):
        self.items = defaultdict(dict)
        self.q = defaultdict(list)

    def addBid(self, userId: int, itemId: int, bidAmount: int) -> None:
        self.items[itemId][userId] = bidAmount
        heapq.heappush(self.q[itemId], (-bidAmount, -userId))

    def updateBid(self, userId: int, itemId: int, newAmount: int) -> None:
        self.items[itemId][userId] = newAmount
        heapq.heappush(self.q[itemId], (-newAmount, -userId))

    def removeBid(self, userId: int, itemId: int) -> None:
        del self.items[itemId][userId]

    def getHighestBidder(self, itemId: int) -> int:
        bid_map = self.items[itemId]
        if not bid_map:
            return -1
        heap = self.q[itemId]
        while heap:
            bid_amount, user_id = -heap[0][0], -heap[0][1]
            if user_id in bid_map and bid_map[user_id] == bid_amount:
                return user_id
            heapq.heappop(heap)
        return -1