class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        left, right = [], deque()
        x = []
        for i in range(len(positions)):
            x.append((positions[i], i, healths[i], directions[i]))
        x.sort()
        for _, i, health, direction in x:
            if direction == 'L':
                while right and health > 0:
                    ri, rh = right.pop()
                    if rh > health:
                        right.append((ri, rh - 1))
                        health = 0
                    elif rh == health:
                        health = 0
                    else:
                        health -= 1
                if health > 0:
                    left.append((i, health))
            else:
                right.append((i, health))
        return [h for i, h in sorted(left + list(right))]