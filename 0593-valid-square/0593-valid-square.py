class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        def square_distance(pt1, pt2):
            return (pt1[0] - pt2[0]) ** 2 + (pt1[1] - pt2[1]) ** 2
        
        p = [p1, p2, p3, p4]
        sd = []
        for i in range(3):
            for j in range(i + 1, 4):
                sd.append(square_distance(p[i], p[j]))

        sd.sort()

        return sd[0] != 0 and sd[0] == sd[1] == sd[2] == sd[3] and sd[4] == sd[5] and sd[4] == 2 * sd[0]