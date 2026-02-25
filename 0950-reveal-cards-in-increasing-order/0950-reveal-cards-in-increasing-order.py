class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        n = len(deck)
        q = deque([i for i in range(n)])
        order = [0] * n
        for i in range(n):
            order[q.popleft()] = i
            if q:
                q.append(q.popleft())
        
        deck.sort()
        
        return [deck[order[i]] for i in range(n)]