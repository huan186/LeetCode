from collections import deque

class FrontMiddleBackQueue:
    def __init__(self):
        self.left = deque()
        self.right = deque()

    def pushFront(self, val: int) -> None:
        self.left.appendleft(val)
        self.__balance()

    def pushMiddle(self, val: int) -> None:
        if len(self.left) > len(self.right):
            self.right.appendleft(self.left.pop())
        self.left.append(val)

    def pushBack(self, val: int) -> None:
        self.right.append(val)
        self.__balance()

    def popFront(self) -> int:
        if not self.left and not self.right:
            return -1

        if self.left:
            val = self.left.popleft()
        else:
            val = self.right.popleft()

        self.__balance()
        return val

    def popMiddle(self) -> int:
        if not self.left:
            return -1

        val = self.left.pop()
        self.__balance()
        return val

    def popBack(self) -> int:
        if self.right:
            val = self.right.pop()
        elif self.left:
            val = self.left.pop()
        else:
            return -1

        self.__balance()
        return val

    def __balance(self):
        if len(self.left) > len(self.right) + 1:
            self.right.appendleft(self.left.pop())
        elif len(self.left) < len(self.right):
            self.left.append(self.right.popleft())

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna