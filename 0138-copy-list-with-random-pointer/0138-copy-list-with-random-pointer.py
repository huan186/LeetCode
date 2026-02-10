"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        mapping = {None: None}
        dummy = Node(0)
        curr = dummy
        while head:
            if head in mapping:
                curr.next = mapping[head]
            else:
                curr.next = Node(head.val)
                mapping[head] = curr.next
            curr = curr.next
            if head.random in mapping:
                curr.random = mapping[head.random]
            else:
                curr.random = Node(head.random.val)
                mapping[head.random] = curr.random
            head = head.next
        return dummy.next