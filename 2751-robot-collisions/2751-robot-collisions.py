class Solution:
    def survivedRobotsHealths(self, positions, healths, directions):
        robots = sorted(range(len(positions)), key=lambda i: positions[i])
        stack = []

        for i in robots:
            if directions[i] == "R":
                stack.append(i)
            else:
                while stack and healths[i] > 0:
                    j = stack[-1]

                    if healths[j] < healths[i]:
                        stack.pop()
                        healths[i] -= 1
                        healths[j] = 0
                    elif healths[j] > healths[i]:
                        healths[j] -= 1
                        healths[i] = 0
                    else:
                        stack.pop()
                        healths[i] = 0
                        healths[j] = 0

        return [h for h in healths if h > 0]