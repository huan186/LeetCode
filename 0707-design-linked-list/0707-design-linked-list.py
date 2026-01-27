class Node:
    def __init__(self, val: int, prv=None, nxt=None):
        self.val = val
        self.prv = prv
        self.nxt = nxt


class MyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        cur = self.head
        for _ in range(index):
            cur = cur.nxt
        return cur.val

    def addAtHead(self, val: int) -> None:
        new = Node(val, None, self.head)
        if self.head:
            self.head.prv = new
        else:
            self.tail = new
        self.head = new
        self.size += 1

    def addAtTail(self, val: int) -> None:
        new = Node(val, self.tail, None)
        if self.tail:
            self.tail.nxt = new
        else:
            self.head = new
        self.tail = new
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        if index == 0:
            self.addAtHead(val)
        elif index == self.size:
            self.addAtTail(val)
        else:
            cur = self.head
            for _ in range(index):
                cur = cur.nxt
            new = Node(val, cur.prv, cur)
            cur.prv.nxt = new
            cur.prv = new
            self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        if index == 0:
            self.head = self.head.nxt
            if self.head:
                self.head.prv = None
            else:
                self.tail = None
        elif index == self.size - 1:
            self.tail = self.tail.prv
            self.tail.nxt = None
        else:
            cur = self.head
            for _ in range(index):
                cur = cur.nxt
            cur.prv.nxt = cur.nxt
            cur.nxt.prv = cur.prv
        self.size -= 1
