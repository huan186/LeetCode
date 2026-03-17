class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        left = right = 0
        moves = 0
        for i, c in enumerate(boxes):
            if c == '1':
                right += 1
                moves += i
        ans = []
        for i, c in enumerate(boxes):
            ans.append(moves)
            if c == '1':
                left += 1
                right -= 1
            moves += left - right
        return ans