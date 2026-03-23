class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        def rotated(original):
            return [list(row) for row in zip(*original[::-1])]
        
        curr = mat
        for _ in range(4):
            if curr == target:
                return True
            curr = rotated(curr)

        return False