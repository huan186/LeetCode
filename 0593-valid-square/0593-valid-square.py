class Solution:
    def validSquare(self, p1, p2, p3, p4):
        def dist(a, b):
            return (a[0]-b[0])**2 + (a[1]-b[1])**2
        
        points = [p1, p2, p3, p4]
        dists = set()
        
        for i in range(4):
            for j in range(i+1, 4):
                d = dist(points[i], points[j])
                if d == 0:
                    return False
                dists.add(d)
        
        return len(dists) == 2