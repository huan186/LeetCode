class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        n = len(deck)
        q = deque(range(n))
        res = [0] * n
        
        for card in deck:
            idx = q.popleft()
            res[idx] = card
            if q:
                q.append(q.popleft())
        
        return res